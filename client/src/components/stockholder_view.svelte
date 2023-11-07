<script>
    import Login from "./login.svelte";
    import AddStocktoWatchlist from "./addStocktoWatchlist.svelte";
    import DeleteStockfromWatchlist from "./deleteStockfromWatchlist.svelte";
    import UpdateInvestment from "./updateInvestment.svelte";

    let logged_in = true;
    let password = "";
    export let username = "username";

    function logout() {logged_in = false;}
    async function change_password() {
        let response = await fetch("/changePassword", {
          method: "POST",
          body: JSON.stringify({
            "username": username,
            "password": password,
          })
        })
        let data = await response.json();
    }
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

    <div id="change-password">
        <form id="change-password-box">
          <label for="password">Change Password: </label>
          <input bind:value={password} type="password" id="pwd" name="pwd">
        </form>
        <button on:click={change_password}>Submit</button>
    </div>
</div>
{:else if logged_in == false}
    <svelte:component this={Login}></svelte:component>
{/if}

