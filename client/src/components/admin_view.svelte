<script>
    import Login from "./login.svelte";

    let logged_in = true;

    function logout() {logged_in = false;}
</script>

{#if logged_in == true}
    Admin View
    <div id="admin-body">
        <div id="logout-div">
            <button on:click={logout}>Logout</button>
        </div>
    </div>
{:else if logged_in == false}
    <svelte:component this={Login}></svelte:component>
{/if}
