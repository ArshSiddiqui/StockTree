<script>
    import Login from "./login.svelte";
    import IndividualStock from "./individual_stock.svelte";

    export let companyName = "company-name";

    // Company Details
    let ceo = "ceo-name";
    let industry = "industry-name";
    let abbreviation = "abbreviation";
    let logged_in = true;
    let password = "";

    function logout() {logged_in = false;}
    async function change_password() {
        let response = await fetch("/changePassword", {
          method: "POST",
          body: JSON.stringify({
            "username": companyName,
            "password": password,
          })
        })
        let data = await response.json();
    }
</script>

{#if logged_in == true}
<div id="company-header">
    
    <div id="logout-div">
        <button on:click={logout}>Logout</button>
    </div>

    <h2>{companyName}</h2>
    
    <div id="company-details">
        <h3>CEO: {ceo}</h3>
        <h3>Industry: {industry}</h3>
        <h3>Primary Stock Abbreviation: {abbreviation}</h3>
    </div>

    <div id="change-password">
        <form id="change-password-box">
          <label for="password">Change Password: </label>
          <input bind:value={password} type="password" id="pwd" name="pwd">
        </form>
        <button on:click={change_password}>Submit</button>
    </div>

    <svelte:component this={IndividualStock}></svelte:component>
</div>
{:else if logged_in == false}
    <svelte:component this={Login}></svelte:component>
{/if}
