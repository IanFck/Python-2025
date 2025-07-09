// Logo de cargando conectado con dashboard
setTimeout(() => {
  window.location.href = 'dashboard_admin.html'; 
}, 6000);

  document.addEventListener('DOMContentLoaded', () => {
    const modo = localStorage.getItem('modoOscuro');
    if (modo === 'true') {
      document.body.classList.add('oscuro');
    }
  });