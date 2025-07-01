document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("resetForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      const email = document.getElementById("email").value;
      const mensaje = document.getElementById("mensaje");

      if (email.includes("@") && email.includes(".")) {
        mensaje.style.color = "green";
        mensaje.textContent = "Si el correo está registrado, recibirás un enlace de recuperación.";
      } else {
        mensaje.style.color = "red";
        mensaje.textContent = "Por favor, ingresa un correo válido.";
      }
    });
  }
});
