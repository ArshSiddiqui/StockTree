<script>
    // import StockView from "./stock_view.svelte";
    //Stockholder would like to add stock to watchlist
    let newStockName = '';
    let newStockPrice = '';
  
    function handleSubmit() {
      // Perform validation and submit the new stock data to the server
      // You can use the fetch API to send a POST request to the server
      const newStockData = {
        name: newStockName,
        symbol: newStockSymbol,
        price: price
      };
  
      fetch('/addStock', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newStockData),
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the server's response, e.g., show a success message
          console.log('Stock added successfully:', data);
        })
        .catch((error) => {
          // Handle errors, e.g., display an error message
          console.error('Error adding stock:', error);
        });
    }
  </script>
  
  <div>
    <h2>Add a New Stock</h2>
    <form on:submit={handleSubmit}>
      <label for="newStockName">Stock Name:</label>
      <input type="text" id="newStockName" bind:value={newStockName} required />
  
      <label for="newStockPrice">Stock Price:</label>
      <input type="text" id="newStockPrice" bind:value={newStockPrice} required />
  
      <button type="submit">Submit</button>
    </form>
  </div>
  