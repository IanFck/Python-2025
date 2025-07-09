document.addEventListener("DOMContentLoaded", () => {
  const usuarios = [
    {
      nombre: "PERSONA 1",
      rol: "TEST",
      accion: "Movió “A” en lugar “X”",
      ultimaVez: "22 de febrero, a las 15:32 P.M."
    },
    {
      nombre: "PERSONA 2",
      rol: "DOCTOR",
      accion: "Salió de la página",
      ultimaVez: "25 de diciembre, a las 16:24 P.M."
    }
  ];

  const tbody = document.querySelector("#history-table tbody");

  // 1. Insertar usuarios con datos
  usuarios.forEach((u) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${u.nombre}</td>
      <td>${u.rol}</td>
      <td>${u.accion}</td>
      <td>${u.ultimaVez}</td>
    `;
    tbody.appendChild(tr);
  });

  // 2. Insertar filas vacías hasta llegar a 10
  const totalFilas = 10;
  const filasFaltantes = totalFilas - usuarios.length;

  for (let i = 0; i < filasFaltantes; i++) {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>&nbsp;</td>
      <td></td>
      <td></td>
      <td></td>
    `;
    tbody.appendChild(tr);
  }
});

  document.addEventListener('DOMContentLoaded', () => {
    const modo = localStorage.getItem('modoOscuro');
    if (modo === 'true') {
      document.body.classList.add('oscuro');
    }
  });