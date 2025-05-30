const banner = document.querySelector('.banner');
const gifExplosao = 'static/img/explosao.gif';

const imagensPeixe = [
   
    { src: 'static/img/peixe1.gif', width: 190, height: 158 },
    { src: 'static/img/peixe2.gif', width: 135, height: 118 },
    { src: 'static/img/peixe3.gif', width: 130, height: 103 },
];

const numPeixes = 12;

for (let i = 0; i < numPeixes; i++) {
    const peixe = document.createElement('div');
    peixe.classList.add('peixe');

    const peixeConfig = imagensPeixe[i % imagensPeixe.length];
    peixe.style.backgroundImage = `url("${peixeConfig.src}")`;
    peixe.style.width = `${peixeConfig.width}px`;
    peixe.style.height = `${peixeConfig.height}px`;

    banner.appendChild(peixe);

    let cliques = 0;

    peixe.addEventListener('click', () => {
        cliques++;
        if (cliques > 10) {
            explodirPeixe(peixe);
        }
    });

    moverPeixe(peixe);
    setInterval(() => moverPeixe(peixe), 3000 + Math.random() * 2000);
}

function moverPeixe(peixe) {
    const margem = 30;
    const bannerWidth = banner.clientWidth;
    const bannerHeight = banner.clientHeight;
    const peixeWidth = peixe.offsetWidth;
    const peixeHeight = peixe.offsetHeight;

    const maxX = bannerWidth - peixeWidth - margem;
    const maxY = bannerHeight - peixeHeight - margem;
    const minX = margem;
    const minY = margem;

    const randomX = Math.random() * (maxX - minX) + minX;
    const randomY = Math.random() * (maxY - minY) + minY;

    const duracao = Math.random() * 3 + 3;
    peixe.style.transition = `top ${duracao}s linear, left ${duracao}s linear`;

    const posicaoAtualX = parseFloat(peixe.style.left) || 0;
    peixe.style.transform = `scaleX(${randomX > posicaoAtualX ? 1 : -1})`;

    peixe.style.left = `${randomX}px`;
    peixe.style.top = `${randomY}px`;
}

function explodirPeixe(peixe) {
    const explosao = document.createElement('img');
    explosao.src = gifExplosao;

    const peixeRect = peixe.getBoundingClientRect();
    const bannerRect = banner.getBoundingClientRect();

    const posX = peixeRect.left - bannerRect.left;
    const posY = peixeRect.top - bannerRect.top;

    explosao.style.position = 'absolute';
    explosao.style.left = `${posX}px`;
    explosao.style.top = `${posY}px`;
    explosao.style.width = `${peixe.offsetWidth}px`;
    explosao.style.height = `${peixe.offsetHeight}px`;
    explosao.style.pointerEvents = 'none';
    explosao.style.zIndex = 999;

    banner.appendChild(explosao);
    peixe.remove();

    setTimeout(() => {
        explosao.remove();
    }, 750);
}
//bolhas abaixo
//bolhas abaixo

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
        img.src = 'static/img/bolha.png';

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