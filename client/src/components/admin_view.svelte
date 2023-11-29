<script>
    import Login from "./login.svelte";

    let logged_in = true;
    let password = "";
    export let username = "username";

    let other_pass = "";
    let other_user = "";

    let num_companies = "";
    let num_stockholders = "";
    let num_admins = "";

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

    async function submit() {
      let response = await fetch("/addUser", {
          method: "POST",
          body: JSON.stringify({
            "username": other_user,
            "password": other_pass,
            "account_type": "admin",
          })
        })
        let data = await response.json();
        if (data["success"] == 1) {
          login_created = true;
        }
    }

    async function get_user_stats() {
        let response = await fetch("/userStatsReports", {
            method: "POST",
            body: JSON.stringify({})
        })
        let data = await response.json();
        num_companies = data['num_companies'];
        num_stockholders = data['num_stockholders'];
        num_admins = data['num_admins'];
    }

    get_user_stats();
</script>

{#if logged_in == true}
    <div id="admin-body">
        <div id="logout-div">
            <button on:click={logout}>Logout</button>
        </div>

        <div id="admin-functionality">
            
            <div id="stats-reports">
                <h4>Statistical Reports on Users</h4>
                <h5>Total number of companies registered as users: {num_companies}</h5>
                <h5>Total number of stockholders registered as users: {num_stockholders}</h5>
                <h5>Total number of admins: {num_admins}</h5>
            </div>

            <div id="signup-center">
                <h4 id="signup-header">Create an Admin Account</h4>
                <form id="signup-box">
                  <label for="username">Username: </label>
                  <input bind:value={other_user} type="text" id="username" name="username"><br>
                  <label for="password">Password: </label>
                  <input bind:value={other_pass} type="password" id="pwd" name="pwd">
                </form>
                <button on:click={submit}>Submit</button>
            </div>
            <br>
            
            <h4>Change Password for {username}</h4>
            <div id="change-password" style={"margin-top:1rem"}>
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
