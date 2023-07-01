<script>
  import Buscador from './componentes/Buscador.svelte'
  import Filtros from './componentes/Filtros.svelte'
  export let resultados;
  let busqueda = '';

  const buscar = async () => {
    // Haz la petición de búsqueda aquí y guarda los resultados en "resultados".
    // Este es solo un ejemplo, deberías cambiarlo para que funcione con tu backend.
    const response = await fetch(`http://localhost:5000/buscar?query=${busqueda}`);
    const data = await response.json();
    resultados = data;
  }
</script>

<Buscador />
<Filtros />

<style>

</style>
