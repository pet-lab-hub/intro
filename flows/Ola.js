// Ola.js
// Código JavaScript para nó função do fluxo "Ola"

var data = new Date(msg.payload);
var dia = data.getDate();
var mes = data.getMonth() + 1;
var ano = data.getFullYear();
var hor = data.getHours().toString().padStart(2, '0');
var min = data.getMinutes().toString().padStart(2, '0');
msg.payload = dia + '/' + mes + '/' + ano 
            + ' ' + hor + ':' + min;
return msg;