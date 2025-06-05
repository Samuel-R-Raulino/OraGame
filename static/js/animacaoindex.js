const banner = document.querySelector('.banner');
const gifExplosao = 'static/img/explosao.gif';

const imagensPeixe = [
    { src: 'static/img/peixe1.gif', width: 190, height: 158 },
    { src: 'static/img/peixe2.gif', width: 135, height: 118 },
    { src: 'static/img/peixe3.gif', width: 130, height: 103 },
];

const imagensNaves = [
    { src: 'static/img/nave1.gif', width: 150, height: 130 },
    { src: 'static/img/nave2.gif', width: 140, height: 120 },
    { src: 'static/img/nave3.gif', width: 160, height: 140 },
];

const numPeixes = 15;
const peixesCriados = [];

for (let i = 0; i < numPeixes; i++) {
    const peixe = document.createElement('div');
    peixe.classList.add('peixe');

    const peixeConfig = imagensPeixe[i % imagensPeixe.length];
    peixe.dataset.index = i % imagensPeixe.length;
    peixe.style.backgroundImage = `url("${peixeConfig.src}")`;
    peixe.style.width = `${peixeConfig.width}px`;
    peixe.style.height = `${peixeConfig.height}px`;

    banner.appendChild(peixe);
    peixesCriados.push(peixe);

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
    const margem = 25;
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

const canvas = document.getElementById('bolhasCanvas');
const ctx = canvas.getContext('2d');

let bolhas = [];
const numBolhas = 15;

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

resizeCanvas();
window.addEventListener('resize', resizeCanvas);

for (let i = 0; i < numBolhas; i++) {
    bolhas.push(criarBolha());
}

function criarBolha() {
    return {
        x: Math.random() * canvas.width,
        y: window.innerHeight + Math.random() * 200,
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

function atualizarPeixesParaTema() {
    const usandoDark = document.body.classList.contains('dark-theme');
    peixesCriados.forEach(peixe => {
        const index = peixe.dataset.index;
        const novaConfig = usandoDark ? imagensNaves[index] : imagensPeixe[index];
        peixe.style.backgroundImage = `url("${novaConfig.src}")`;
        peixe.style.width = `${novaConfig.width}px`;
        peixe.style.height = `${novaConfig.height}px`;
    });
}

const botaoTema = document.getElementById('botaoTema');
const bolhasCanvas = document.getElementById('bolhasCanvas');
const transitionOverlay = document.getElementById('transitionOverlay');
const iconeSwitch = document.getElementById('iconeSwitch');

const logoOragame = document.getElementById('logoOragame');
const logoOragameGrande = document.getElementById('logoOragameGrande');

const imgSol = "static/img/sol.png";
const imgLua = "static/img/lua.png";

const logoClaro = "static/img/oragame.png";
const logoEscuro = "static/img/oradark.png";

let transitionDuration = 800;
let switchCooldown = 2000;

function atualizarIcone() {
    iconeSwitch.style.backgroundImage = botaoTema.checked ? `url('${imgLua}')` : `url('${imgSol}')`;
}

function atualizarLogo() {
    const isDark = document.body.classList.contains('dark-theme');
    const novaSrc = isDark ? logoEscuro : logoClaro;
    logoOragame.src = novaSrc;
    logoOragameGrande.src = novaSrc;
}

function atualizarBolhasCanvas() {
    bolhasCanvas.style.display = document.body.classList.contains('dark-theme') ? 'none' : 'block';
}

function salvarTema() {
    const temaAtual = document.body.classList.contains('dark-theme') ? 'dark' : 'light';
    localStorage.setItem('tema', temaAtual);
}

function carregarTema() {
    const temaSalvo = localStorage.getItem('tema');
    if (temaSalvo === 'dark') {
        document.body.classList.add('dark-theme');
        botaoTema.checked = true;
    } else {
        document.body.classList.remove('dark-theme');
        botaoTema.checked = false;
    }
}

function initTema() {
    carregarTema();
    atualizarIcone();
    atualizarLogo();
    atualizarBolhasCanvas();
    atualizarPeixesParaTema();
}



botaoTema.addEventListener('change', () => {
    botaoTema.disabled = true;
    atualizarIcone();

    const isDark = document.body.classList.contains('dark-theme');
    transitionOverlay.style.background = isDark ? 'white' : 'black';
    transitionOverlay.style.transition = `opacity ${transitionDuration}ms ease-in-out`;
    transitionOverlay.style.opacity = '1';

    setTimeout(() => {
        document.body.classList.toggle('dark-theme');

        atualizarPeixesParaTema();
        atualizarLogo();
        atualizarBolhasCanvas();
        salvarTema();

        setTimeout(() => {
            transitionOverlay.style.opacity = '0';
        }, 50);
    }, transitionDuration);

    setTimeout(() => {
        botaoTema.disabled = false;
    }, switchCooldown);
});

initTema();