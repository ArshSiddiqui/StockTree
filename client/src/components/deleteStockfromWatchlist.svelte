<script>
    let deleteStockName = "";
    async function deleteStockClient() {
        await fetch('/deleteStock', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            "stockName": deleteStockName,
            })
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
    <form on:submit={deleteStockClient}>
        <label for="stockName">Stock to delete:</label>
        <input id="stockName" bind:value={deleteStockName}>
        <input type="submit" value="Submit"/> 
    </form>
</div>