// temperatura-media.js
// Código JavaScript para nó função do fluxo "Temp-Media"


// No início
// ---------
context.set("n_temp", 0);
context.set("soma_temp", 0);
context.set("n_temp", 0);
context.set("soma_temp", 0);


// Na mensagem
// -----------
var temp = msg.payload;
// Acrescenta temp à soma_temp e atualiza contexto
var soma = context.get("soma_temp") + temp;
context.set("soma_temp", soma);

// Incrementa contagem e atualiza contexto
var n = context.get("n_temp") + 1;
context.set("n_temp", n);

// Calcula média e atualiza payload
var media = 0;
media = soma / n;
msg.payload = media.toFixed(2);

return msg;
