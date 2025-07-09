document.getElementById('loginForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const rutIngresado = document.getElementById('rut').value.trim();
  const claveIngresada = document.getElementById('password').value.trim();

  try {
    const response = await fetch('datos.json');
    const data = await response.json();
    const usuarios = data.usuarios;

    const usuarioEncontrado = usuarios.find(user => user.rut === rutIngresado);

    // RUT y Contraseña incorrectas
    if (!usuarioEncontrado) {
      document.getElementById('error').textContent = 'RUT no registrado';
      return;
    }

    if (usuarioEncontrado.contraseña !== claveIngresada) {
      document.getElementById('error').textContent = '!CONTRASEÑA INCORRECTA!';
      return;
    }

    // RUT y contraseña correctos
    localStorage.setItem('rutActivo', usuarioEncontrado.rut);

    if (usuarioEncontrado.rut === '22287173-5') {
      window.location.href = 'dashboard_admin.html';
    } else {
      window.location.href = 'dashboard.html';
    }

    //Error en caso de no verificar usuario
  } catch (error) {
    console.error('Error al verificar usuario:', error);
    document.getElementById('error').textContent = 'Error al cargar los datos';
  }
});
  

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
