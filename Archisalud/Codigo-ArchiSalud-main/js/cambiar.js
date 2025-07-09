document.addEventListener('DOMContentLoaded', () => {
const form = document.getElementById('cambiarForm');
const mensaje = document.getElementById('mensaje');

form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const nueva = document.getElementById('nueva').value;
    const confirmar = document.getElementById('confirmar').value;
    const rutActivo = localStorage.getItem('rutActivo');


    // Error si las contraseñas ingresadas no coinciden una con la otra
    if (nueva !== confirmar) {
    mensaje.textContent = "Las contraseñas no coinciden.";
    mensaje.style.color = "red";
    return;
    }

    try {
    const res = await fetch('datos.json');
    const data = await res.json();
    const usuario = data.usuarios.find(user => user.rut === rutActivo);

    // Contraseña cambiada
    if (usuario) {
        mensaje.textContent = "Contraseña cambiada exitosamente. Redirigiendo...";
        mensaje.style.color = "green";

        setTimeout(() => {
        window.location.href = "index.html";
        }, 2000);
        // Usuario no encontrado
    } else {
        mensaje.textContent = "Usuario no encontrado.";
        mensaje.style.color = "red";
    }
    // Error al cargar datos
    } catch (error) {
    console.error(error);
    mensaje.textContent = "Error al cargar los datos.";
    mensaje.style.color = "red";
    }
});
});

function modoOscuro() {
  document.getElementById('modal-config').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

function cerrarModal() {
  document.getElementById('modal-config').style.display = 'none';
  document.getElementById('overlay').style.display = 'none';
}
// Modo oscuro
function cambiarModo() {
  const body = document.body;
  const modal = document.getElementById('modal-config');
  const label = document.getElementById('modo-label');
  const isDark = body.classList.toggle('oscuro');
  modal.classList.toggle('dark');
  label.textContent = isDark ? "Cambiar a modo Claro" : "Cambiar a modo Oscuro";

  // Guardar en localStorage
  localStorage.setItem('modoOscuro', isDark ? 'true' : 'false');
}

// Recuperar estado del modo al cargar
window.onload = () => {
  const modoGuardado = localStorage.getItem('modoOscuro');
  if (modoGuardado === 'true') {
    document.body.classList.add('oscuro');
    document.getElementById('modo-toggle').checked = true;
    document.getElementById('modal-config').classList.add('dark');
    document.getElementById('modo-label').textContent = "Cambiar a modo Claro";
  }
}

// Al cargar la página, aplicar el modo oscuro si está activado
document.addEventListener('DOMContentLoaded', () => {
  const modo = localStorage.getItem('modoOscuro');
  if (modo === 'true') {
    document.body.classList.add('oscuro');
  }
});
