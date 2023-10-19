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

<h1>{text}</h1>
<button on:click={connect}>Connect</button>
<button on:click={getAllStocks}>GetAllStocks</button>
<p>{allStocks}</p>