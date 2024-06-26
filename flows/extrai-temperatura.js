// extrai-temperatura.js
// Código JavaScript para nó função do fluxo "MQTT Data"

// Na mensagem
// -----------
const obj = msg.payload;
var temp = obj.temperatura;
msg.payload = temp + '°C/';
return msg;