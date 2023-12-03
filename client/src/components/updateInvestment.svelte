<script>
    // import StockView from "./stock_view.svelte";
    //Stockholder would like to add stock to watchlist
    export let newInvestmentName = '';
    export let newInvestmentSymbol = '';
  
  </script>
  
  <div>
    <h2>Update Investment</h2>
    <form on:submit={handleUpdateInvestment}>
      <label for="newStockName">Stock Name:</label>
      <input type="text" id="newStockName" bind:value={newStockName} required />
  
      <label for="newStockSymbol">New Investment:</label>
      <input type="text" id="newStockSymbol" bind:value={newStockSymbol} required />
  
      <button type="submit">Submit</button>
    </form>
  </div>
  