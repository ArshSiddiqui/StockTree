<script>
    import Login from "./login.svelte";
    import IndividualStock from "./individual_stock.svelte";
    import IndividualCountry from "./individual_country.svelte";

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

    // Competitor Details
    let display_competitor = false;
    let competitor_name = "name";
    let competitor_price = "price";
    let competitor_open = "open";
    let competitor_ask = "ask";
    let competitor_day_range = "day-range";
    let competitor_volume = "volume";
    let competitor_company_name = "";
    let comp_full_name = "name";
    let competitor_financial_market = "financial-market";
    let competitor_bid = "bid";

    // Country details
    let display_country = false;
    let country_name = "";
    let country_full_name = "name";
    let unemployment_rate = 0;
    let gdp = 0;
    let inflation_rate = 0;
    let population = 0;



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

    async function get_competitor_details() {
        let response = await fetch("/getStock", {
            method: "POST",
            body: JSON.stringify({
                "company_name": competitor_company_name,
            })
        })
        let data = await response.json();
        competitor_name = data['abbreviation'];
        competitor_price = data['price'];
        competitor_open = data['open'];
        competitor_ask = data['ask'];
        competitor_day_range = data['day_range'];
        competitor_volume = data['volume'];
        comp_full_name = data['cname'];
        competitor_bid = data['bid'];
        competitor_financial_market = data['fmarket'];
        display_competitor = true;
    }

    function close_competitor_view(){display_competitor=false;}

    async function get_country_details() {
        let response = await fetch("/getCountryDetails", {
            method: "POST",
            body: JSON.stringify({
                "country_name": country_name,
            })
        })
        let data = await response.json();
        country_full_name = data['name'];
        unemployment_rate = data['unemployment_rate'];
        gdp = data['gdp'];
        inflation_rate = data['inflation_rate'];
        population = data['population'];
        display_country = true;
    }

    function close_country_view(){display_country=false;}

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

    
    <h3>View Competitor Details</h3>
    <div id="competitor-view">
        <form id="view-competitor-data">
            <label for="competitor-name">Competitor Name: </label>
            <input bind:value={competitor_company_name} type="competitor_name" id="comp_name" name="comp_name">
        </form>
        <button on:click={get_competitor_details}>Get Details</button>
    </div>
    {#if display_competitor}
        <button on:click={close_competitor_view}>Close Competitor View</button>
        <svelte:component this={IndividualStock} name={competitor_name} price={competitor_price} open={competitor_open} 
                                                ask={competitor_ask} day_range={competitor_day_range}
                                                volume={competitor_volume} company_name={comp_full_name}
                                                financial_market={competitor_financial_market} bid={competitor_bid}>
                                            </svelte:component>

    {/if}

    <h3>View Country Economic Trends</h3>
    <div id="country-view">
        <form id="view-company-details">
            <label for="country-name">Country name: </label>
            <input bind:value={country_name} type="country_name">
        </form>
        <button on:click={get_country_details}>Get Economic Trends</button>
    </div>
    {#if display_country}
        <button on:click={close_country_view}>Close Country View</button>
        <svelte:component this={IndividualCountry} name={country_full_name} unemployment_rate={unemployment_rate}
                                                    gdp={gdp} inflation_rate={inflation_rate}
                                                    population={population}></svelte:component>
    {/if}


    <h3>Change Company Account Details:</h3>
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
