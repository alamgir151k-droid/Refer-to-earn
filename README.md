<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Earn Platform Demo</title>
<style>
body {font-family:Arial, sans-serif;background:#f5f6fa;margin:0;padding:0;}
header {background:#1e40af;color:white;padding:15px;text-align:center;}
.container {max-width:1000px;margin:30px auto;background:white;border-radius:10px;padding:20px;box-shadow:0 0 10px rgba(0,0,0,.1);}
h2 {border-bottom:2px solid #1e40af;padding-bottom:5px;color:#1e40af;}
button {background:#2563eb;color:white;border:none;padding:8px 16px;border-radius:6px;cursor:pointer;}
button:hover{background:#1e3a8a;}
input,select {padding:8px;margin:5px;width:100%;border-radius:6px;border:1px solid #ccc;}
nav {background:#1e40af;padding:10px;text-align:center;}
nav a {color:white;text-decoration:none;margin:0 15px;font-weight:bold;}
nav a:hover{text-decoration:underline;}
.table {width:100%;border-collapse:collapse;margin-top:10px;}
.table th,.table td {border:1px solid #ccc;padding:8px;text-align:left;}
.table th {background:#1e40af;color:white;}
.section{display:none;}
.active{display:block;}
.stat-box{display:flex;justify-content:space-around;margin:10px 0;}
.card{background:#f3f4f6;border-radius:10px;padding:15px;text-align:center;flex:1;margin:5px;}
.card h3{margin:5px 0;color:#1e40af;}
</style>
</head>
<body>

<header><h1>💰 Earn Platform Demo</h1></header>

<nav>
  <a href="#" onclick="showSection('login')">Login</a>
  <a href="#" onclick="showSection('signup')">Sign Up</a>
  <a href="#" onclick="showSection('dashboard')">Dashboard</a>
  <a href="#" onclick="showSection('admin')">Admin</a>
</nav>

<div class="container">
  <!-- LOGIN -->
  <div id="login" class="section active">
    <h2>User Login</h2>
    <input type="email" placeholder="Email">
    <input type="password" placeholder="Password">
    <button>Login</button>
  </div>

  <!-- SIGNUP -->
  <div id="signup" class="section">
    <h2>Create Account</h2>
    <input type="text" placeholder="Full Name">
    <input type="email" placeholder="Email">
    <input type="password" placeholder="Password">
    <button>Sign Up</button>
  </div>

  <!-- DASHBOARD -->
  <div id="dashboard" class="section">
    <h2>User Dashboard</h2>
    <div class="stat-box">
      <div class="card"><h3>$0</h3><p>Total Balance</p></div>
      <div class="card"><h3>$0</h3><p>Daily Earnings</p></div>
      <div class="card"><h3>None</h3><p>Active Plan</p></div>
    </div>

    <h3>Available Plans</h3>
    <table class="table">
      <tr><th>Plan</th><th>Price</th><th>Daily Earning</th><th>Action</th></tr>
      <tr><td>Basic</td><td>₹500</td><td>₹50</td><td><button>Purchase</button></td></tr>
      <tr><td>Standard</td><td>₹1000</td><td>₹100</td><td><button>Purchase</button></td></tr>
      <tr><td>Premium</td><td>₹1500</td><td>₹170</td><td><button>Purchase</button></td></tr>
    </table>

    <h3>Deposit</h3>
    <input type="text" placeholder="Amount">
    <button>Deposit</button>

    <h3>Withdraw</h3>
    <input type="text" placeholder="Amount">
    <button>Withdraw</button>
  </div>

  <!-- ADMIN PANEL -->
  <div id="admin" class="section">
    <h2>Admin Panel</h2>
    <input type="email" placeholder="Admin Email">
    <input type="password" placeholder="Password">
    <button onclick="loginAdmin()">Login as Admin</button>

    <div id="adminContent" style="display:none;">
      <div class="stat-box">
        <div class="card"><h3>10</h3><p>Total Users</p></div>
        <div class="card"><h3>₹5000</h3><p>Total Deposits</p></div>
        <div class="card"><h3>₹1200</h3><p>Total Withdrawals</p></div>
      </div>

      <h3>User List</h3>
      <table class="table">
        <tr><th>User</th><th>Plan</th><th>Status</th><th>Action</th></tr>
        <tr><td>@AliKhan</td><td>Basic</td><td>Pending</td>
          <td><button>Approve</button> <button>Reject</button></td></tr>
        <tr><td>@Sara</td><td>Premium</td><td>Approved</td>
          <td><button>Reject</button></td></tr>
      </table>

      <h3>Add New Plan</h3>
      <input type="text" placeholder="Plan Name">
      <input type="number" placeholder="Price">
      <input type="number" placeholder="Daily Earning">
      <button>Add Plan</button>
    </div>
  </div>
</div>

<script>
function showSection(id){
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}

function loginAdmin(){
  alert("Demo login successful (UI only)");
  document.getElementById("adminContent").style.display="block";
}
</script>

</body>
</html>
