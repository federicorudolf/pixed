<script>
  export let id;
  export let imagen;
  export let titulo;
  export let descripcion;
</script>

<div class="contenido-tarjeta">
  <img src={imagen} alt={titulo} />
  <h2>{titulo}</h2>
  <p>{descripcion}</p>
</div>

<style>
  .contenido-tarjeta {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    cursor: pointer;
  }

  .contenido-tarjeta img {
    width: 100%;
    height: auto;
  }

  .contenido-tarjeta h2 {
    font-size: 18px;
    margin: 10px 0;
  }

  .contenido-tarjeta p {
    font-size: 14px;
    color: #777;
  }
</style>
