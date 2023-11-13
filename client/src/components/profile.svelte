<!-- Profile.svelte -->
<script>
  let showProfile = false;

  function toggleProfile() {
    showProfile = !showProfile;
  }
</script>

<div class="profile-dropdown">
  <button on:click={toggleProfile}>User Profile</button>
  {#if showProfile}
    <div class="profile-content">
      <img src="images/profile.jpg" alt="Profile Image" />
      <p>Username: username</p>
      <p>Email: email@example.com</p>
    </div>
  {/if}
</div>

<style>
  .profile-dropdown {
    position: relative;
    display: flex;
    justify-content: flex-end;
    margin: 10px;
  }

  button {
    background: none;
    border: none;
    cursor: pointer;
    text-decoration: underline;
  }

  .profile-content {
    position: absolute;
    top: 0;
    right: 0;
    background-color: #fff;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    padding: 10px;
    text-align: center;
    display: none;
  }

  .profile-content img {
    max-width: 100px;
  }

  .profile-dropdown:hover .profile-content {
    display: block;
  }
</style>
