import os
import logging
import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "@YourChannel")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "123456789").split(",")]

# Default reward settings
JOIN_BONUS = int(os.getenv("JOIN_BONUS", 10))
REFERRAL_BONUS = int(os.getenv("REFERRAL_BONUS", 20))
MIN_WITHDRAW_POINTS = int(os.getenv("MIN_WITHDRAW_POINTS", 300))
POINT_TO_PKR_RATE = float(os.getenv("POINT_TO_PKR_RATE", 0.5))

# Database setup
DB_PATH = os.getenv("DB_PATH", "referral_bot.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    points INTEGER DEFAULT 0,
    referred_by INTEGER
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS withdraw_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    points INTEGER,
    method TEXT,
    account TEXT,
    status TEXT DEFAULT 'pending'
)""")
conn.commit()

# Helper functions
def add_points(user_id: int, points: int):
    cursor.execute("INSERT OR IGNORE INTO users (user_id, points) VALUES (?, 0)", (user_id,))
    cursor.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, user_id))
    conn.commit()

def get_points(user_id: int):
    cursor.execute("SELECT points FROM users WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    return row[0] if row else 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    cursor.execute("INSERT OR IGNORE INTO users (user_id, points) VALUES (?, 0)", (user.id,))
    if args:
        ref_id = int(args[0])
        if ref_id != user.id:
            cursor.execute("UPDATE users SET referred_by=? WHERE user_id=? AND referred_by IS NULL", (ref_id, user.id))
            add_points(ref_id, REFERRAL_BONUS)
            await context.bot.send_message(chat_id=ref_id, text=f"🎉 آپ کو {REFERRAL_BONUS} پوائنٹس ملے ریفرل بونس کے طور پر!")
    add_points(user.id, JOIN_BONUS)
    await update.message.reply_text(f"👋 خوش آمدید {user.first_name}! آپ کو {JOIN_BONUS} پوائنٹس ملے ہیں سائن اپ بونس کے طور پر۔")

async def points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    pts = get_points(user.id)
    pkr = pts * POINT_TO_PKR_RATE
    await update.message.reply_text(f"💰 آپ کے پوائنٹس: {pts}\n🇵🇰 PKR: {pkr} روپے")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    pts = get_points(user.id)
    if pts < MIN_WITHDRAW_POINTS:
        await update.message.reply_text(f"❌ کم از کم {MIN_WITHDRAW_POINTS} پوائنٹس چاہیے ودڈرال کے لیے۔")
        return
    if len(context.args) < 2:
        await update.message.reply_text("⚠️ استعمال: /withdraw method account\nمثال: /withdraw easypaisa 03001234567")
        return
    method, account = context.args[0], context.args[1]
    cursor.execute("INSERT INTO withdraw_requests (user_id, points, method, account) VALUES (?, ?, ?, ?)", (user.id, pts, method, account))
    cursor.execute("UPDATE users SET points=0 WHERE user_id=?", (user.id,))
    conn.commit()
    for admin_id in ADMIN_IDS:
        await context.bot.send_message(chat_id=admin_id, text=f"📥 Withdraw Request\nUser: {user.id}\nMethod: {method}\nAccount: {account}\nPoints: {pts}")
    await update.message.reply_text("✅ آپ کی ودڈرال ریکویسٹ ایڈمن کو بھیج دی گئی ہے۔")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("points", points))
    app.add_handler(CommandHandler("withdraw", withdraw))
    app.run_polling()

if __name__ == "__main__":
    main(
