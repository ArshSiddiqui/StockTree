<script>
  export let allStocks = [];
  

</script>
<div>
    <h2>Stocks</h2>
    <table>
      <thead>
            <th>Ticker</th>
            <th>Shares owned</th>
      </thead>
      <tbody>
            {#each allStocks as stock}
            <tr>
              <th>{stock[0]}</th>
              <th>{stock[1]}</th>
            </tr>
            {/each}
      </tbody>
    </table>
</div>