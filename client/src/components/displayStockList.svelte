<script>
   $: allStocks = fetch("./fetchName")
      .then(d => d.text())
      .then(d => allStocks = d);

</script>
<div>
    <h2>Stocks</h2>
    <p>{allStocks}</p>
    <!--
    <table>
      <thead>
          <tr>
              <th colspan="2">Stocks</th>
          </tr>
      </thead>
      <tbody>
        {#each allStocks as stock}
          <tr>
              <th>{stock}</th>
          </tr>
        {/each}
      </tbody>
    </table-->
</div>