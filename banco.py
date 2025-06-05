import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

# Criar a tabela de jogos (adicionando personagem_principal)
cursor.execute('''
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preço REAL,
    descrição TEXT NOT NULL,
    img1 TEXT,
    img2 TEXT,
    img3 TEXT,
    requisitos TEXT,
    classificação TEXT,
    download_id TEXT,
    personagem_principal TEXT
)
''')

# Função para gerar nomes de imagens
def img_name(nome, n):
    return nome.lower().replace(" ", "_") + str(n)

# Jogos para inserir
jogos = [
    {
        "nome": "Quake",
        "preço": 0.0,
        "descrição": """Quake é um jogo de computador de tiro em primeira pessoa, criado pela Id Software e lançado em 1996. Devido à sua popularidade, ele se tornaria o primeiro jogo da série Quake, tendo sido bem recebido pelo público e crítica, levando às continuações Quake II, Quake III Arena, Quake 4 e Enemy Territory: Quake Wars, com a série Quake vendendo 4 milhões de cópias.""",
        "requisitos": """PROCESSADOR: Processador Intel Pentium(R) 75 MHz ou superior
MEMÓRIA RAM: DOS -- Requer 8 MB de RAM Win 95 -- Requer 16 MB de RAM
PLACA DE VÍDEO: Tela compatível com VGA ou melhor
S.O: Sistema operacional MS-DOS 5.0 ou superior ou Windows(R) 95/98
ESPAÇO: Unidade de disco rígido com 80 MB de espaço não compactado disponível
PLACA DE SOM: placa de som 100% compatível com Sound Blaster
DISCO ÓPTICO: Unidade de CD-ROM de velocidade dupla (300 K/s, taxa de transferência sustentada)
INTERNET: Suporta reprodução de modem, rede e Internet
PERIFÉRICO: Suporte para joystick e mouse (recomenda-se mouse de 3 botões)""",
        "classificação": "18+",
        "download_id": "",
        "personagem_principal": "o Quake Guy"
    },
    {
        "nome": "Prince of Persia",
        "preço": 0.0,
        "descrição": """Prince of Persia é uma franquia de videogame criada por Jordan Mechner. É centrado em uma série de jogos de ação e aventura focados em várias encarnações do príncipe homônimo, ambientados na Pérsia antiga e medieval.""",
        "requisitos": """Sistema Operacional: MS-DOS (versões antigas)
Processador: Intel 80286 ou superior
Memória RAM: 512 KB ou mais
Placa de Vídeo: CGA, EGA ou VGA (dependendo da versão do jogo)
Armazenamento: Disquete de 3,5" ou 5,25" (dependendo da versão)""",
        "classificação": "12+",
        "download_id": "",
        "personagem_principal": "o príncipe do game Prince of Persia"
    },
    {
        "nome": "Resident Evil 1",
        "preço": 0.0,
        "descrição": """Resident Evil é um jogo de survival horror de 1996 desenvolvido e publicado pela Capcom para o PlayStation. É o primeiro jogo da franquia Resident Evil da Capcom. Situado na fictícia região montanhosa de Arklay, no Centro-Oeste, os jogadores controlam Chris Redfield e Jill Valentine, membros da força-tarefa de elite S.T.A.R.S., que devem escapar de uma mansão infestada de zumbis e outros monstros.""",
        "requisitos": """Sistema Operacional: Windows 10 ou 11
Processador: 2,0 GHz
Memória RAM: 2 GB
Placa de Vídeo: Compatível com DirectX 9.0c
DirectX: Versão 11
Espaço em Disco: 650 MB disponível""",
        "classificação": "18+",
        "download_id": "",
        "personagem_principal": "Jill Valentine"
    },
    {
        "nome": "Wolfenstein 3D",
        "preço": 0.0,
        "descrição": """Wolfenstein 3D (1992), é uma re-imaginação do cenário de Castle Wolfenstein numa perspectiva de primeira pessoa com ênfase no combate directo. Stealth e opções não-violentas não estão presentes. Silas Warner, o designer dos jogos originais para Apple II, não esteve envolvido na produção.""",
        "requisitos": """Sistema Operacional: DOS 6.0 ou Windows 95
Processador: Pentium 75 MHz
Memória RAM: 16 MB
Placa de Vídeo: SVGA com 1 MB de VRAM
CD-ROM: 4x ou mais rápido
Som: Placa de som compatível com Sound Blaster
Espaço em Disco: Cerca de 80 MB
Teclado e mouse: Requeridos""",
        "classificação": "18+",
        "download_id": "",
        "personagem_principal": "Blazkowicz BJ"
    }
]

# Inserir jogos no banco
for jogo in jogos:
    nome_formatado = jogo["nome"].lower().replace(" ", "_")
    img1 = nome_formatado + "1"
    img2 = nome_formatado + "2"
    img3 = nome_formatado + "3"

    cursor.execute(
        '''INSERT INTO games 
        (nome, preço, descrição, img1, img2, img3, requisitos, classificação, download_id, personagem_principal)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (
            jogo["nome"],
            jogo["preço"],
            jogo["descrição"],
            img1,
            img2,
            img3,
            jogo["requisitos"],
            jogo["classificação"],
            jogo["download_id"],
            jogo["personagem_principal"]
        )
    )

conn.commit()

print("Jogos adicionados com sucesso!")

# Exibir os jogos do banco
cursor.execute('SELECT * FROM games')
games = cursor.fetchall()

print("\nJogos no banco:")
for game in games:
    print(game)

conn.close()
