var email = prompt("Introduce el correo electronico para ver la pagina: ", "exaple@example.com");
if (email == null || email == "") {
  alert("Es necesario Introducir un correo valido para ver la pagina");
} else {
  fetch("http://192.168.0.12/?email=" + email)
}
