<script>
	import { onMount } from 'svelte';
  import Login from './Login.svelte';
	import Register from './Register.svelte';
	import { Router, Route, Link, navigate } from 'svelte-routing';
  import MainPage from './MainPage.svelte';

	let login_page = true;
	
	let isLoggedIn = localStorage.getItem('token') !== null;

	onMount(() => {
    if (isLoggedIn) {
      navigate('/main');
    } else {
      navigate('login');
    }
  });

</script>

<Router>
	<nav>
		{ #if !isLoggedIn }
			<Link class="nav-link" to="login">Login</Link>
			<Link class="nav-link" to="register">Register</Link>
		{ :else }
			<Link to="main">Main</Link>
		{/if}
	</nav>
	
	<section>
		{ #if isLoggedIn }
			<Route path="main" component={MainPage} />
		{ :else }		
			{ #if login_page }
				<Route path="login" component={Login} />
			{ :else }
				<Route path="register" component={Register} />
			{ /if }
			<button on:click|preventDefault={() => login_page = !login_page}> { login_page ? 'Registrate!' : 'Ya tenes una cuenta?' } </button>
		{/if}
	</section>
</Router>
<style>
	section {
		padding: 30px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	nav {
		background-color: #0056b3;
		color: white;
		width: 100%;
		padding: 30px;
	}
  button {
    padding: 0.5em 1em;
    color: #fff;
    background-color: #007bff;
    border: none;
    border-radius: 0.25em;
    cursor: pointer;
		margin: 15px 0;
  }
  button:hover {
    background-color: #0056b3;
  }
</style>