<script>
    import StockholderView from "./stockholder_view.svelte";
    import CompanyView from "./company_view.svelte";
    import SignupView from "./signup_view.svelte";
    import IndividualStock from "./individual_stock.svelte";

    let logged_in = false;
    let signup_in = false;
    let user_type = "";
    export let username = "";
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

    function signup() {
      signup_in = true;
      logged_in = true;
      console.log(signup_in)
    }
</script>

{#if logged_in == false}
    <div id="login-center">
      <form id="login-box">
        <label for="username">Username: </label>
        <input bind:value={username} type="text" id="username" name="username"><br>
        <label for="password">Password: </label>
        <input bind:value={password} type="password" id="password" name="pwd">
      </form>
      <button on:click={login}>Login</button>
      <button on:click={signup}>Sign up</button>
      <svelte:component this={IndividualStock}></svelte:component>
    </div>
{:else if logged_in == true && user_type == "Stockholder"}
    <svelte:component this={StockholderView}></svelte:component>
{:else if logged_in == true && user_type == "Company"}
    <svelte:component this={CompanyView} companyName={username}></svelte:component>
{:else if signup_in == true}
    <svelte:component this={SignupView}></svelte:component>
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