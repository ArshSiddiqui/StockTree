<script>
    import Login from "./login.svelte";
    import DisplayStockList from "./displayStockList.svelte";
    import SearchCountry from "./searchCountry.svelte";
    import Profile from "./profile.svelte";

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

    let newCountryName = '';
    let countryGDP = '';
    let countryInflation = '';
    let countryUnemployment = '';
    let displayCountry = false;
   
  
    function handleNewCountry() {
      // Perform validation and submit the new country data to the server
      // You can use the fetch API to send a POST request to the server
      const newCountry = {
        name: newCountryName,
      };
  
      fetch('/getNewCountry', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newCountry),
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the server's response, e.g., show a success message
          countryGDP = data['gdp']
          countryInflation = data['infl_rate']
          countryUnemployment = data['unempl_rate']
          displayCountry = true;

          console.log('Country searched successfully:', data);
        })
        .catch((error) => {
          // Handle errors, e.g., display an error message
          console.error('Error searching for country:', error);
        });
    }

    let newInvestmentName = '';
    let newInvestmentSymbol = '';
    let price = 0;
  
    function handleUpdateInvestment() {
      // Perform validation and submit the new stock data to the server
      // You can use the fetch API to send a POST request to the server
      const newStockData = {
        name: newInvestmentName,
        symbol: newInvestmentSymbol,
        price: price
      };
  
      fetch('/updateInvestment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newStockData),
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the server's response, e.g., show a success message
          console.log('Stock added successfully:', data);
        })
        .catch((error) => {
          // Handle errors, e.g., display an error message
          console.error('Error adding stock:', error);
        });
    }
</script>

{#if logged_in == true}
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
      <form on:submit={handleUpdateInvestment}>
        <label for="newStockName">Stock Name:</label>
        <input type="text" id="newStockName" bind:value={newInvestmentName} required />
    
        <label for="newStockSymbol">New Investment:</label>
        <input type="text" id="newStockSymbol" bind:value={newInvestmentSymbol} required />
    
        <button type="submit">Submit</button>
      </form>
    </div>
    <br/><br/>
    <form on:submit={handleNewCountry}>
      <label for="countryName">Country Name:</label>
      <input type="text" id="newCountryName" bind:value={newCountryName} required />
  
      <button type="submit">Submit</button>
    </form>
    <svelte:component this={SearchCountry} newCountryName={newCountryName} countryGDP={countryGDP} countryInflation={countryInflation} countryUnemployment={countryUnemployment} displayCountry={displayCountry}></svelte:component>

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

