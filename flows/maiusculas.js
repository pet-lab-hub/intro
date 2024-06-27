// maiusculas.js
// Código JavaScript para nó função do fluxo "Bom dia"

// Na mensagem
// -----------
var mensagem = msg.payload;
// converte mensagem em maiúsculas
msg.payload = mensagem.toUpperCase();
return msg;