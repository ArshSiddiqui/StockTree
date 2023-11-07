<script>
    import Login from "./login.svelte";
    import IndividualStock from "./individual_stock.svelte";

    export let companyName = "company-name";

    // Company Details
    let ceo = "ceo-name";
    let industry = "industry-name";
    let abbreviation = "abbreviation";
    let logged_in = true;

    function logout() {logged_in = false;}
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

    <svelte:component this={IndividualStock}></svelte:component>
</div>
{:else if logged_in == false}
    <svelte:component this={Login}></svelte:component>
{/if}
