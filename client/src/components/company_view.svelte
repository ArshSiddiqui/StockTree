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
    let country = "country-name";

    let company_chart_ctx;
    let company_chart;
    let competitor_chart;

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
    let gdp_per_capita = 0;

    // Employee Details
    let num_employees = "";
    let highest_salaried_empyloyee = ""
    let lowest_salaried_employee = ""
    let average_salary = ""

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

    async function get_employee_stats() {
        let response = await fetch("/emplStatsReports", {
            method: "POST",
            body: JSON.stringify({
                "company_name": companyName,
            })
        })
        let data = await response.json();
        if (data["data"] == "true") {
            num_employees = data["num_empl"];
            highest_salaried_empyloyee = data["highest_empl"];
            lowest_salaried_employee = data["lowest_empl"];
            average_salary = data["avg_salary"];
        } else {
            num_employees = "0";
        }
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
        country = data['country'];
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
        get_historical_data(comp_full_name, false);
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
        if(data['message'] != "success") {
            let response = await fetch("/getNewCountry", {
                method: "POST",
                body: JSON.stringify({
                    "name": country_name,
                })
            })
            let data = await response.json();
            country_full_name = data['name'];
            unemployment_rate = data['unemployment_rate'];
            gdp = data['gdp'];
            inflation_rate = data['inflation_rate'];
            display_country = true;
        }
        else {
            country_full_name = data['name'];
            unemployment_rate = data['unemployment_rate'];
            gdp = data['gdp'];
            inflation_rate = data['inflation_rate'];
            population = data['population'];
            gdp_per_capita = data['gdp_per_capita'];
            display_country = true;
        }
    }

    function close_country_view(){display_country=false;}

    async function get_historical_data(comp_name, curr_comp) {
        let response = await fetch("/getHistoricalStockData", {
            method: "POST",
            body: JSON.stringify({
                "company_name": comp_name,
            })
        })
        let data = await response.json();
        let historical_data = data['historical_data'].split(",");
        let dates = data['dates'].split(";");
        let totalData = []
        for (let i = 0; i < dates.length; i++) {
            totalData[i] = {x:dates[i], y:historical_data[i]};
        }
        
        if (curr_comp) {
           company_chart_ctx = company_chart.getContext('2d');
        } else {
            company_chart_ctx = competitor_chart.getContext('2d');
        }
        new Chart(company_chart_ctx, {
            type: "line",
            data: {
                labels: dates,
                datasets: [{
                    label: 'Value of stock over time',
                    fill: false,
                    borderColor: "#213a1b",
                    pointRadius: 4,
                    pointBackgroundColor: "rgba(0,0,0,1)",
                    data: totalData
                }] 
            },
            options: {
                scales: {
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'Closing Value of Stock'
                        }
                    }],
                    xAxes: [{
                        ticks: {
                            reverse: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Date',
                        }
                    }]
                }
            }
        });
    }

    get_company_details();
    get_stock();
    get_historical_data(companyName, true);
    get_employee_stats();
    get_country_details();
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
        <h3>Country: {country}</h3>
    </div>

    <div id="employee-details">
        {#if num_employees !== "0"}
            <h4>Number of {companyName} employees registered with StockTree: {num_employees}</h4>
            <h4>Highest salaried employee: {highest_salaried_empyloyee}</h4>
            <h4>Lowest salaried employee: {lowest_salaried_employee}</h4>
            <h4>Average salary: {average_salary}</h4>
        {:else}
            <h4>No registered employees with {companyName} in StockTree.</h4>
        {/if}
    </div>

    <div id="comp-details">
    <svelte:component this={IndividualStock} name={name} price={price} open={open} ask={ask} day_range={day_range}
                                                volume={volume} company_name={company_name}
                                                financial_market={financial_market} bid={bid}>
                                            </svelte:component>
    <div id="company-chart">
        <canvas bind:this={company_chart} id="historical-chart"></canvas>
    </div>
    </div>

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
        <div id="competitor-chart">
            <canvas bind:this={competitor_chart} id="historical-chart"></canvas>
        </div>

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
                                                    gdp={gdp} gdp_per_capita={gdp_per_capita} inflation_rate={inflation_rate}
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
