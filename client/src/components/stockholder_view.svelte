Stockholder View

<script>
    import AddStocktoWatchlist from "./addStocktoWatchlist.svelte";
    import DeleteStockfromWatchlist from "./deleteStockfromWatchlist.svelte";
    import UpdateInvestment from "./updateInvestment.svelte";
</script>

<svelte:component this={AddStocktoWatchlist}></svelte:component>
<br/><br/>
<svelte:component this={DeleteStockfromWatchlist}></svelte:component>
<br/><br/>
<svelte:component this={UpdateInvestment}></svelte:component>
