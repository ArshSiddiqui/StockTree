<script>
  let text = "Not Connected"
  let allStocks = ""

  function connect() {
    fetch("./connect")
      .then(d => d.text())
      .then(d => (text = d));
  }

  function getAllStocks() {
    fetch("./fetch")
      .then(d => d.text())
      .then(d => allStocks = d)
  }
</script>

<div id="login-center">
  <form id="login-box">
    <label for="username">Username: </label>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password: </label>
    <input type="password" id="pwd" name="pwd">
  </form>
  <button on:click={connect}>Connect</button>
  <h3>{text}</h3>
  <button on:click={getAllStocks}>GetAllStocks</button>
  <p>{allStocks}</p>
</div>

