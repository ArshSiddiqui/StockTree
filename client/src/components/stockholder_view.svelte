<script>
    import Login from "./login.svelte";
    import DisplayStockList from "./displayStockList.svelte";
    import SearchCountry from "./searchCountry.svelte";
    import Profile from "./profile.svelte";
    import IndividualCountry from "./individual_country.svelte";


    let logged_in = true
    let password = "";
    export let username = "username";

    // Country details
    let display_country = false;
    let country_name = "";
    let country_full_name = "name";
    let unemployment_rate = 0;
    let gdp = 0;
    let inflation_rate = 0;
    let population = 0;
    let gdp_per_capita = 0;

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
                    "country_name": country_name,
                })
            })
            let data = await response.json();
        }
        country_full_name = data['name'];
        unemployment_rate = data['unemployment_rate'];
        gdp = data['gdp'];
        inflation_rate = data['inflation_rate'];
        population = data['population'];
        gdp_per_capita = data['gdp_per_capita'];
        display_country = true;
    }

    function close_country_view(){display_country=false;}



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

  let allStocks = '';
  async function getName() {
    let response = await fetch("./fetchName", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }});
    let nameData = await response.text();
    console.log(nameData);
    nameData = nameData.slice(2,-2);
    allStocks = nameData.split("\", \"");
  }
  getName();

  let newStockName = '';
    let newStockPrice = '';
  
    function handleAddStock() {
      // Perform validation and submit the new stock data to the server
      // You can use the fetch API to send a POST request to the server
      const newStockData = {
        name: newStockName,
        symbol: newStockSymbol,
        price: price
      };
  
      fetch('/addStockToWatchlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newStockData),
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the server's response, e.g., show a success message
          if(response['is_added'] == true) {
            console.log('Stock added successfully:', data);
            getName();
          }
        })
        .catch((error) => {
          // Handle errors, e.g., display an error message
          console.error('Error adding stock:', error);
        });
    }

    let deleteStockName = "";
    async function deleteStockClient() {
        await fetch('/deleteStock', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            "stockName": deleteStockName,
            })
      })
      .then((response) => response.json())
        .then((data) => {
          // Handle the server's response, e.g., show a success message
          if (data.is_deleted == "true") {
            console.log('Stock deleted successfully');
          } else {
            console.log('Stock could not be deleted');
          }
        });
    }

    let newInvestmentAmt = '';
    let newInvestmentSymbol = '';
  
    async function handleUpdateInvestment() {
      // Perform validation and submit the new stock data to the server
      // You can use the fetch API to send a POST request to the server
      console.log("here!!!");
      let response = await fetch("/updateInvestment", {
            method: "POST",
            body: JSON.stringify({
                "name": newInvestmentSymbol,
                "amt": newInvestmentAmt,
                "username": username
            })
      })
      // let data = await response.json();
   }
</script>

{#if logged_in == true}
<div id="all-stockholder">
<div>
    <div id="logout-div">
        <button on:click={logout}>Logout</button>
        <svelte:component this={Profile}></svelte:component>
    </div>
    <svelte:component this={DisplayStockList} allStocks={allStocks}></svelte:component>
    <br/><br/>
    <div>
      <h2>Add a New Stock</h2>
      <form on:submit={handleAddStock}>
        <label for="newStockName">Stock Name:</label>
        <input type="text" id="newStockName" bind:value={newStockName} required />
    
        <label for="newStockPrice">Stock Price:</label>
        <input type="text" id="newStockPrice" bind:value={newStockPrice} required />
    
        <button type="submit">Submit</button>
      </form>
    </div>
    <br/><br/>
    
<div>
  <h2>Delete a stock from the watchlist</h2>
  <form on:submit={deleteStockClient}>
      <label for="stockName">Stock to delete:</label>
      <input id="stockName" bind:value={deleteStockName}>
      <input type="submit" value="Submit"/> 
  </form>
</div>
    <br/><br/>
    <div>
      <h2>Update Investment</h2>
      <form id="upt-stck">
        <label for="sname">Stock Ticker: </label>
        <input bind:value={newInvestmentSymbol} type="stockname" id="stockname" name="stockname">
        <label for="invAmt">Investment Amount:</label>
        <input bind:value={newInvestmentAmt} type="amtInt" id="amtInv" name="amtInv">
      </form>
      <button on:click={handleUpdateInvestment}>Submit</button>
    </div>

    <br/><br/>

    <h2>View Country Economic Trends</h2>
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



    <br/>

    <div id="change-password">
        <form id="change-password-box">
          <label for="password">Change Password: </label>
          <input bind:value={password} type="password" id="pwd" name="pwd">
        </form>
        <button on:click={change_password}>Submit</button>
    </div>
</div>
</div>
{:else if logged_in == false}
    <svelte:component this={Login}></svelte:component>
{/if}

