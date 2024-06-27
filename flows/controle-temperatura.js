// controle-temperatura.js
// Código JavaScript para nó função do fluxo "MQTT Data"

// Na mensagem
// -----------
if (msg.payload > 24) {
	msg.payload = "ligar";
} else {
	msg.payload = "desligar";
}
return msg;