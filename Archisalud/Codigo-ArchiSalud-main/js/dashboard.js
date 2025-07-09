function modoOscuro() {
  document.getElementById('modal-config').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

function cerrarModal() {
  document.getElementById('modal-config').style.display = 'none';
  document.getElementById('overlay').style.display = 'none';
}

function cambiarModo() {
  const body = document.body;
  const modal = document.getElementById('modal-config');
  const label = document.getElementById('modo-label');
  const isDark = body.classList.toggle('oscuro');
  modal.classList.toggle('dark');
  label.textContent = isDark ? "Cambiar a modo Claro" : "Cambiar a modo Oscuro";

  localStorage.setItem('modoOscuro', isDark ? 'true' : 'false');
}

// Al cargar la página, aplicar el modo oscuro si está activado
document.addEventListener('DOMContentLoaded', () => {
  const modo = localStorage.getItem('modoOscuro');
  if (modo === 'true') {
    document.body.classList.add('oscuro');
  }
});
