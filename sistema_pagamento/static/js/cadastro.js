
// Função que retorna o valor de um campo de formulário, dado seu seletor (ex: '#email')
function linkarDado(id) {
    let input = document.querySelector(id); // Seleciona o elemento pelo ID
    return input.value; // Retorna o valor preenchido no input
}

// Função que valida se o dado tem pelo menos um número mínimo de caracteres
function validarDado(dado, minimo) {
    return dado.length >= minimo; // Retorna true se o comprimento for suficiente
}

// Função que verifica se a senha e a confirmação são iguais
function confirmarSenha(senha, confirmSenha) {
    return senha === confirmSenha; // Retorna true se as senhas forem idênticas
}

// Função que valida se o e-mail possui um formato válido usando regex
function validarEmail(email) {
    let regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Expressão regular básica para validar e-mails
    return regexEmail.test(email); // Retorna true se o e-mail for válido
}

// Função principal de cadastro
function cadastrar() {
    let usuario = linkarDado('#usuario');
    let email = linkarDado('#email');
    let senha = linkarDado('#senha');
    let confirmSenha = linkarDado('#confirmSenha');

    let validUsuario = validarDado(usuario, 4);
    let validEmail = validarEmail(email);
    let validSenha = validarDado(senha, 8);
    let validConfirmSenha = confirmarSenha(senha, confirmSenha);

    if (validUsuario && validEmail && validSenha && validConfirmSenha) {
        // Enviar dados para o servidor Flask via POST
        fetch('/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                usuario: usuario,
                email: email,
                senha: senha
            })
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '/home'; // Redireciona se sucesso
            } else {
                alert('Erro ao cadastrar. Tente novamente.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    } else {
        console.log("Erro: dados inválidos.");
    }
}


// Captura os elementos de "mostrar/ocultar senha"
let verSenha = document.querySelector('#verSenha');
let verConfirmSenha = document.querySelector('#verConfirmSenha');

// Adiciona evento de clique para alternar a visibilidade da senha
verSenha.addEventListener('click', () => {
    let inputSenha = document.querySelector('#senha');

    // Alterna entre mostrar e esconder a senha
    if (inputSenha.getAttribute('type') === 'password') {
        inputSenha.setAttribute('type', 'text'); // Mostra a senha
    } else {
        inputSenha.setAttribute('type', 'password'); // Oculta a senha
    }
});

// Adiciona evento de clique para alternar a visibilidade da confirmação da senha
verConfirmSenha.addEventListener('click', () => {
    let inputConfirmSenha = document.querySelector('#confirmSenha');

    // Alterna entre mostrar e esconder a confirmação da senha
    if (inputConfirmSenha.getAttribute('type') === 'password') {
        inputConfirmSenha.setAttribute('type', 'text'); // Mostra a confirmação
    } else {
        inputConfirmSenha.setAttribute('type', 'password'); // Oculta a confirmação
    }
});
