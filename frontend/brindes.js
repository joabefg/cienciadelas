const codigosBrindes = {
    CIENCIA2026: "Chaveiro Ciência",
    MARIECURIE: "Chaveiro DNA",
    JAQUELINE: "Chaveiro Cientista",
    CIENCIADELAS: "Chaveiro Personalizado",
    CIENTISTA: "Camiseta Ciência Delas"
};

const campoCodigo = document.getElementById("codigoBrinde");
const botaoResgatar = document.getElementById("btnResgatar");
const mensagem = document.getElementById("mensagemResgate");

botaoResgatar.addEventListener("click", function () {
    const codigo = campoCodigo.value.trim().toUpperCase();

    if (!codigo) {
        mensagem.textContent = "Digite um código para continuar.";
        mensagem.style.color = "#B61606";
        return;
    }

    if (codigosBrindes[codigo]) {
        mensagem.textContent =
            "Código válido! Recompensa desbloqueada: " +
            codigosBrindes[codigo] + ".";
        mensagem.style.color = "#00FE00";
        campoCodigo.value = "";
    } else {
        mensagem.textContent = "Código inválido ou inexistente.";
        mensagem.style.color = "#B61606";
    }
});
