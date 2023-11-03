Stockholder View

<script>
    import Login from "./login.svelte";
    import AddStocktoWatchlist from "./addStocktoWatchlist.svelte";
    import DeleteStockfromWatchlist from "./deleteStockfromWatchlist.svelte";
</script>

<svelte:component this={AddStocktoWatchlist}></svelte:component>
<br/><br/>
<svelte:component this={DeleteStockfromWatchlist}></svelte:component>

