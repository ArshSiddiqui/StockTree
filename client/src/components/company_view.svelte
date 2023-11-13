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

    // Stock Details
    let name = "stock-name";
    let price = "price";
    let open = "open";
    let ask = "ask";
    let day_range = "day-range";
    let volume = "volume";
    let company_name = "company-name";
    let financial_market = "financial-market";
    let bid = "bid";


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

    async function get_stock() {
        let response = await fetch("/getStock", {
            method: "POST",
            body: JSON.stringify({
                "company_name": companyName,
            })
        })
        let data = await response.json();
        name = data['abbreviation'];
        price = data['price'];
        open = data['open'];
        ask = data['ask'];
        day_range = data['day_range'];
        volume = data['volume'];
        company_name = data['cname'];
        bid = data['bid'];
        financial_market = data['fmarket'];
    }

    async function get_company_details() {
        let response = await fetch("/companyDetails", {
            method: "POST",
            body: JSON.stringify({
                "company_name": companyName,
            })
        })
        let data = await response.json();
        ceo = data['ceo'];
        industry = data['industry'];
        abbreviation = data['abbreviation'];
    }

    get_company_details();
    get_stock();
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

    <svelte:component this={IndividualStock} name={name} price={price} open={open} ask={ask} day_range={day_range}
                                                volume={volume} company_name={company_name}
                                                financial_market={financial_market} bid={bid}>
                                            </svelte:component>

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
