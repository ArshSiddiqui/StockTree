<script>
    import StockholderView from "./stockholder_view.svelte";

    let logged_in = false;

    function login() {
       logged_in = true;
    }
</script>

{#if logged_in == false}
    <div id="login-center">
      <form id="login-box">
        <label for="username">Username: </label>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password: </label>
        <input type="password" id="pwd" name="pwd">
      </form>
      <button on:click={login}>Login</button>
    </div>
{:else}
    <svelte:component this={StockholderView}></svelte:component>
{/if}