document.addEventListener("DOMContentLoaded", () => {
  const especialidades = [
    { nombre: "Unidad de paciente crítico", total: 15, url: "unidad_paciente_critico.html" },
    { nombre: "Obstetricia y ginecología",  total: 12, url: "obstetricia.html" },
    { nombre: "Neonatología",               total: 10, url: "neonatologia.html" },
    { nombre: "Unidad de Tratamiento Intermedio Pediátrico", total: 8, url: "pediatrico.html" },
    { nombre: "Medicina",                   total: 20, url: "medicina.html" },
    { nombre: "Cirugía",                    total: 18, url: "cirugia.html" },
    { nombre: "Psiquiatría",                total: 14, url: "psiquiatria.html" },
    { nombre: "Pensionado",                 total: 6,  url: "pensionado.html" },
    { nombre: "Urgencia",                   total: 8,  url: "urgencia.html" },
    { nombre: "Observación urgencia",       total: 10, url: "observacion.html" }
  ];

  const header = document.createElement("header");
  header.innerHTML = `
    <div class="header-wrap">
      <a href="dashboard.html">
        <i class='bx bx-undo salir'></i>
      </a>
      <h1>ESTATUS DE CAMAS.</h1>
    </div>
  `;
  document.body.appendChild(header);

  const tabla = document.createElement("table");
  const thead = document.createElement("thead");
  const tbody = document.createElement("tbody");

  thead.innerHTML = `
    <tr>
      <th>ESPECIALIDAD</th>
      <th>CAMAS TOTALES</th>
      <th>CAMAS OCUPADAS</th>
      <th>ESTADO</th>
    </tr>
  `;

  especialidades.forEach(({ nombre, total, url }) => {
    const tr = document.createElement("tr");

    const tdEsp = document.createElement("td");
    tdEsp.textContent = nombre;

    const tdTot = document.createElement("td");
    tdTot.innerHTML = `<strong>${total}</strong>`;

    const tdOcup = document.createElement("td");
    const input = document.createElement("input");
    input.type = "number";
    input.min = 0;
    input.max = total;
    input.value = 0;
    input.style.width = "4rem";
    tdOcup.appendChild(input);

    const tdEstado = document.createElement("td");
    const btn = document.createElement("button");
    btn.className = "estado-btn";
    btn.textContent = "▼";

    btn.addEventListener("click", () => {
      window.location.href = url;
    });

    tdEstado.appendChild(btn);

    tr.append(tdEsp, tdTot, tdOcup, tdEstado);
    tbody.appendChild(tr);
  });

  tabla.append(thead, tbody);
  document.body.appendChild(tabla);
});

  document.addEventListener('DOMContentLoaded', () => {
    const modo = localStorage.getItem('modoOscuro');
    if (modo === 'true') {
      document.body.classList.add('oscuro');
    }
  });