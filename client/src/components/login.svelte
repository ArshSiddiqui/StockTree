<script>
    import StockholderView from "./stockholder_view.svelte";
    import CompanyView from "./company_view.svelte";

    let logged_in = false;
    let user_type = "";
    let username = "";
    // $: alterego = username === "" ? "": "evil " + username;
    let password = "";

    async function login() {
      let response = await fetch("/login", {
        method: "POST",
        body: JSON.stringify({
          "username": username,
          "password": password,
        })
      })
      let data = await response.json();
      logged_in = data["valid_password"];
      user_type = data["user_type"];
    }
</script>

{#if logged_in == false}
    <div id="login-center">
      <form id="login-box">
        <label for="username">Username: </label>
        <input bind:value={username} type="text" id="username" name="username"><br>
        <label for="password">Password: </label>
        <input bind:value={password} type="password" id="pwd" name="pwd">
      </form>
      <button on:click={login}>Login</button>
    </div>
{:else if logged_in == true && user_type == "Stockholder"}
    <svelte:component this={StockholderView}></svelte:component>
{:else if logged_in == true && user_type == "Company"}
    <svelte:component this={CompanyView}></svelte:component>
{/if}

<!-- Your input username is {username}. -->
<!-- Your alter ego is {alterego}. -->

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
</style>