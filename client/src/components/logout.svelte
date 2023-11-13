<script>
    import Login from "./login.svelte";

    let logged_in = true;

    function logout() {
        logged_in = true;
    }

    function reload_page() {
        history.go(0);
    }
</script>

{#if logged_in == true}
<div id="logout-div">
    <button on:click={logout}>Logou</button>
</div>
{:else if logged_in == false}
    <!-- <svelte:component this={Login}></svelte:component> -->
    {history.go(0)}
{/if}