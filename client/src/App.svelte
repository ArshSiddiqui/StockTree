<script>
  let text = "Not Connected"

  function connect() {
    fetch("./connect")
      .then(d => d.text())
      .then(d => (text = d));
  }
</script>

<h1>{text}</h1>
<button on:click={connect}>Connect</button>
