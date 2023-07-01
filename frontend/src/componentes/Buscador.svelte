<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let busqueda = '';

  function buscar(e) {
    e.preventDefault();
    dispatch('buscar', busqueda);
  }
</script>

<form on:submit={buscar}>
  <input bind:value={busqueda} type="text" placeholder="Buscar..." />
  <button type="submit">Buscar</button>
</form>

<style>
  form {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  form input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  form button {
    padding: 10px 20px;
    border: none;
    background-color: #007BFF;
    color: white;
    border-radius: 4px;
    cursor: pointer;
  }
</style>

