<script>
    $: allStocks = fetch("./fetch")
      .then(d => d.text())
      .then(d => allStocks = d);
    $: console.log(allStocks);
    let stockName = "";
    function deleteStockClient() {
        let stockJson = JSON.stringify({name: stockName});
        fetch('/deleteStock', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
        body: stockJson,
      })
      .then((response) => response.json())
        .then((data) => {
          // Handle the server's response, e.g., show a success message
          if (data.is_deleted == "true") {
            console.log('Stock deleted successfully');
          } else {
            console.log('Stock could not be deleted');
          }
        });
    }
</script>

<div>
    <h2>Delete a stock from the watchlist</h2>
    <p>{allStocks}</p>
    <form on:submit={deleteStockClient}>
        <label for="stockName">Stock to delete:</label>
        <input id="stockName" bind:value={stockName}>
        <button type="submit"/> 
    </form>
</div>