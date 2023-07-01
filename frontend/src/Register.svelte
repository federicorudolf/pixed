<script>
  let email = '';
  let name = '';
  let password = '';
  let repeat_password = '';
  let adult_email = '';

  async function register() {
    const response = await fetch('http://127.0.0.1:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, email, password, adult_email })
    });
    
    if (response.ok) {
      const { access_token } = await response.json();
      localStorage.setItem('token', access_token);
      navigate('/main');
    } else {
      console.error('Error de registro');
    }
  }
</script>

<form on:submit|preventDefault={register}>
  <label for="name">Nombre </label>
  <input id="name" bind:value={name} required>

  <label for="email">Email</label>
  <input id="email" bind:value={email} required>

  <label for="password">Contraseña</label>
  <input id="password" type="password" bind:value={password} required>

  <label for="password">Repetir Contraseña</label>
  <input id="password" type="password" bind:value={repeat_password} required class={ password !== repeat_password ? 'border-red' : '' }>

  <label for="adult_email">Email del adulto responsable</label>
  <input id="adult_email" type="adult_email" bind:value={adult_email} required>

  <button type="submit" disabled={ password !== repeat_password }>Registrarse</button>
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