<script>
    import Login from "./login.svelte";
    import AddStocktoWatchlist from "./addStocktoWatchlist.svelte";
    import DeleteStockfromWatchlist from "./deleteStockfromWatchlist.svelte";
    import UpdateInvestment from "./updateInvestment.svelte";
    // import Logout from "./logout.svelte";

    let logged_in = true;

    function logout() {logged_in = false;}
</script>

{#if logged_in == true}
<div>
    Stockholder View
    <div id="logout-div">
        <button on:click={logout}>Logout</button>
    </div>
    <svelte:component this={AddStocktoWatchlist}></svelte:component>
    <br/><br/>
    <svelte:component this={DeleteStockfromWatchlist}></svelte:component>
    <br/><br/>
    <svelte:component this={UpdateInvestment}></svelte:component>
</div>
{:else if logged_in == false}
    <svelte:component this={Login}></svelte:component>
{/if}

