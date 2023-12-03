<script>
    // import StockView from "./stock_view.svelte";
    //Stockholder would like to add stock to watchlist
    export let newCountryName = '';
    export let countryGDP = '';
    export let countryInflation = '';
    export let countryUnemployment = '';
    export let displayCountry = false;
   

  </script>
  
  <div>
    <h2>Search Country</h2>
    {#if displayCountry}
    <table>
      <thead></thead>
      <tbody><tr>
        <th>{newCountryName}</th>
        <th>{countryGDP}</th>
        <th>{countryInflation}</th>
        <th>{countryUnemployment}</th>
      </tr></tbody>
    </table>
    {/if}
  </div>
  
  