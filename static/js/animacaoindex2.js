const canvas = document.getElementById('bolhasCanvas');
const ctx = canvas.getContext('2d');

let bolhas = [];
const numBolhas = 15;

// Ajusta o tamanho do canvas
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight; // ou só window.innerHeight
}

resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Criação inicial das bolhas
for (let i = 0; i < numBolhas; i++) {
    bolhas.push(criarBolha());
}

function criarBolha() {
    return {
        x: Math.random() * canvas.width,
        y: window.innerHeight + Math.random() * 200,  // Respawn sempre abaixo da tela
        size: Math.random() * 100 + 50,
        speed: Math.random() * 1 + 0.5,
        drift: Math.random() * 2 - 1,
        opacity: Math.random() * 0.5 + 0.5
    };
}


function desenharBolhas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    bolhas.forEach(bolha => {
        ctx.globalAlpha = bolha.opacity;
        const img = new Image();
        img.src = 'statio/img/bolha.png';

        ctx.drawImage(img, bolha.x, bolha.y, bolha.size, bolha.size);
    });

    ctx.globalAlpha = 1;
}

function atualizarBolhas() {
    bolhas.forEach(bolha => {
        bolha.y -= bolha.speed;
        bolha.x += bolha.drift;

        if (bolha.y + bolha.size < 0) {
            Object.assign(bolha, criarBolha());
        }
    });
}

function animar() {
    atualizarBolhas();
    desenharBolhas();
    requestAnimationFrame(animar);
}

animar();