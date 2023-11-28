<script>
    // import StockView from "./stock_view.svelte";
    //Stockholder would like to add stock to watchlist
    let newCountryName = '';
   
  
    function handleSubmit() {
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
          console.log('Country searched successfully:', data);
        })
        .catch((error) => {
          // Handle errors, e.g., display an error message
          console.error('Error searching for country:', error);
        });
    }
  </script>
  
  <div>
    <h2>Search Country</h2>
    <form on:submit={handleSubmit}>
      <label for="countryName">Country Name:</label>
      <input type="text" id="newCountryName" bind:value={newCountryName} required />
  
      <button type="submit">Submit</button>
    </form>
  </div>
  
  