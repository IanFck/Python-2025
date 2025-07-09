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

async function confirmarDatos() {
  const nombre = document.getElementById("nombre").value.trim();
  const rut = document.getElementById("rut").value.trim();

  try {
    const res = await fetch("pacientes.json");
    const data = await res.json();

    const encontrado = data.find(p => p.nombre === nombre && p.rut === rut);

      //Si conciden los datos, generara una alerta de paciente encontrado
    if (encontrado) {
      alert("Paciente encontrado.");
    } else {
      //Si no, dara otra alerta con un mensaje de paciente no encontrado
      alert("Paciente NO encontrado.");
    }
    //En caso de error de archivo JSON
  } catch (error) {
    console.error("Error al cargar el JSON:", error);
    alert("Error al cargar datos.");
  }
}
function realizarDerivacion() {
  window.location.href = "confirmacion.html";
}

setTimeout(() => {
  console.log("Hola después de 3 segundos");
}, 3000);


// Al cargar la página, aplicar el modo oscuro si está activado
document.addEventListener('DOMContentLoaded', () => {
  const modo = localStorage.getItem('modoOscuro');
  if (modo === 'true') {
    document.body.classList.add('oscuro');
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const botones = document.querySelectorAll(".seleccionar-btn");

  botones.forEach(boton => {
    boton.addEventListener("click", (e) => {
      e.preventDefault(); // Evita comportamiento por defecto si es formulario
      
      // Elimina la clase 'seleccionado' de todos los hospitales
      document.querySelectorAll(".hospital-card").forEach(card => {
        card.classList.remove("seleccionado");
      });

      // Agrega la clase al contenedor del botón clickeado
      const hospitalCard = boton.closest(".hospital-card");
      hospitalCard.classList.add("seleccionado");
    });
  });
});
