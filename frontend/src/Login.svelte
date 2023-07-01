<script>
import { navigate } from 'svelte-routing';
  let email = '';
  let password = '';
  async function submitForm() {
    const response = await fetch('http://127.0.0.1:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const { access_token } = await response.json();
      localStorage.setItem('token', access_token);
      navigate('/main');
    } else {
      console.log('Fallo el inicio de sesion');
    }
  }
</script>


<form on:submit|preventDefault={submitForm}>
  <label for="email">Email
    <input name="email" type="text" bind:value={email} required>
  </label>
  <label for="password">Password
    <input name="password" type="password" bind:value={password} required>
  </label>
  <button type="submit"> Log in </button>

</form>
<style>
  form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 300px;
    margin: 0 auto;
    padding: 2em;
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    border-radius: 0.25em;
  }
  label {
    margin-bottom: 0.5em;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
    width: 100%;
  }
  input {
    margin-left: 10px;
    padding: 0.25em;
    border: 1px solid #ced4da;
    border-radius: 0.25em;
    align-self: start;
  }
  button {
    padding: 0.5em 1em;
    color: #fff;
    background-color: #007bff;
    border: none;
    border-radius: 0.25em;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
</style>