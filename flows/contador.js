// contador.js
// Código JavaScript para nó função do fluxo "MQTT Count"

// No início
// ----------
// O código adicionado aqui será executado
// sempre que o nó for iniciado.
contexto.set("num_msg", 0);


// Na mensagem
// -----------
// Recupera num_msg do contexto
var num_msg = context.get("num_msg");
// Incrementa valor
num_msg = num_msg + 1;
// Salva num_msg no contexto
contexto.set("num_msg", num_msg);
// Atualiza payload
msg.payload = num_msg;
return msg;