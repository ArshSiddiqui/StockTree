<script>
    import Login from "./login.svelte";

    let username = "";
    let password = "";
    let login_created = false;
    let user_type = "";

    async function submit() {
      if (user_type == "") {
        return;
      } else {
        let response = await fetch("/addUser", {
          method: "POST",
          body: JSON.stringify({
            "username": username,
            "password": password,
            "account_type": user_type,
          })
        })
        let data = await response.json();
        if (data["success"] == 1) {
          login_created = true;
        }
      }
    }
</script>

{#if login_created == false}
    <div id="signup-center">
        <h3 id="signup-header">Create a StockTree Account</h3>
        <form id="signup-box">
          <label for="username">Username: </label>
          <input bind:value={username} type="text" id="username" name="username"><br>
          <label for="password">Password: </label>
          <input bind:value={password} type="password" id="pwd" name="pwd">
          <label for="type">Type:</label>
          <select bind:value={user_type} for="type">
            <option value="stockholder">Stockholder</option>
            <option value="company">Company</option>
          </select>
        </form>
        <button on:click={submit}>Submit</button>
    </div>
{:else}
    <svelte:component this={Login}></svelte:component>
{/if}

<style>
  div {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
  }

  button {
    cursor: pointer;
  }

  h3 {
    color: #213a1b;
    font-family: 'Hind Siliguri';
    font-size: x-large;
  }

  select {
    border: none;
    border-radius: 10px;
    background-color: #ccd9c9;
    font-size: large;
  }

  option {
    font-size: large;
    font-family: 'Hind Siliguri';
  }

  #signup-box {
	font-family: 'Hind Siliguri';
	font-size: large;
	margin-bottom: 1rem;
  }
</style>