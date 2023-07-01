<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let fecha_creacion = '';
  let dificultad = '';
  let tipo_contenido = '';

  function actualizarFiltros() {
    dispatch('actualizarFiltros', { fecha_creacion, dificultad, tipo_contenido });
  }
</script>

<div>
  <label>
    Fecha de Creación:
    <input bind:value={fecha_creacion} type="date" on:input={actualizarFiltros} />
  </label>

  <label>
    Dificultad:
    <select bind:value={dificultad} on:input={actualizarFiltros}>
      <option value="">- Seleccione una dificultad -</option>
      <option value="facil">Fácil</option>
      <option value="intermedio">Intermedio</option>
      <option value="dificil">Difícil</option>
    </select>
  </label>

  <label>
    Tipo de contenido:
    <select bind:value={tipo_contenido} on:input={actualizarFiltros}>
      <option value="">- Seleccione un tipo -</option>
      <option value="audiovisual">Audiovisual</option>
      <option value="juego">Juego</option>
      <option value="lectura">Lectura</option>
    </select>
  </label>
</div>

<style type="text/css">
  div {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }

  div label {
    display: flex;
    flex-direction: column;
    font-size: 14px;
    color: #777;
  }

  div input, div select {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>