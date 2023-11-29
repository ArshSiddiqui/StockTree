<script>
    $: allStocks = fetch("./fetchName")
      .then(d => d.text())
    $: console.log(allStocks);
</script>

<div>
    <h2>Stocks</h2>
    <p>{allStocks}</p>
    <!--{#each allStocks as name}
      <p>{name}</p><br/>
    {/each}-->
</div>