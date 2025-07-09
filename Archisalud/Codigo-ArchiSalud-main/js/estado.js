const estados = ["Disponible", "Ocupado"];
const tbody = document.getElementById("tabla-camas");
const cantidadCamas = parseInt(document.body.getAttribute("data-camas"));

for (let i = 1; i <= cantidadCamas; i++) {
  const fila = document.createElement("tr");

  const codigo = document.createElement("td");
  codigo.textContent = i.toString().padStart(3, '0');

  const estado = document.createElement("td");
  const select = document.createElement("select");
  estados.forEach(e => {
    const option = document.createElement("option");
    option.value = e;
    option.text = e;
    select.appendChild(option);
  });
  estado.appendChild(select);

  const fecha = document.createElement("td");
  const inputFecha = document.createElement("input");
  inputFecha.type = "date";
  fecha.appendChild(inputFecha);

  const datos = document.createElement("td");
  const inputDatos = document.createElement("input");
  inputDatos.type = "text";
  inputDatos.placeholder = "Nombre u observaciones";
  datos.appendChild(inputDatos);

  fila.appendChild(codigo);
  fila.appendChild(estado);
  fila.appendChild(fecha);
  fila.appendChild(datos);

  tbody.appendChild(fila);
}

  document.addEventListener('DOMContentLoaded', () => {
    const modo = localStorage.getItem('modoOscuro');
    if (modo === 'true') {
      document.body.classList.add('oscuro');
    }
  });
