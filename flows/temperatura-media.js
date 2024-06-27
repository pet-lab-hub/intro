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
var soma = context.get("soma_temp") + temp;
context.set("soma_temp", soma);

var n = 1 + context.get("n_temp");
context.set("n_temp", n);
var media = 0;
if (n > 0) {
    media = soma / n;
    msg.payload = media;
} else {
    msg.payload = "N/D";
}

return msg;