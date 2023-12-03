<script>
  export let allStocks = [];
  

</script>
<div>
    <h2>Stocks</h2>
    <table>
      <thead>
      </thead>
      <tbody>
            {#each allStocks as stock}
              <tr><th>{stock}</th></tr>
            {/each}
      </tbody>
    </table>
</div>