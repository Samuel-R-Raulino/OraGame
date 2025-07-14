function mostrarMensagem() {
    alert("Você clicou no botão!");
}

function abrirPopup() {
    document.getElementById("popupEscolha").style.display = "block";
}

function fecharPopup() {
    document.getElementById("popupEscolha").style.display = "none";
}

function selecionarAvatar(nomeArquivo) {
    fetch('/atualizar-avatar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ avatar: nomeArquivo })
    })
    .then(response => {
        if (response.ok) {
            document.querySelector('.pfp').src = `/static/img/pfp/${nomeArquivo}`;
            fecharPopup();
        }
    });
}

