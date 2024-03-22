# VARIÁVEIS GLOBAIS:
personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara

# MENU:
def menu():
    i = "0"

    while i != "2":
        print("Bem vindo a humanos vs capivaras")
        print("""
    Menu:
            1- Jogar
            2- Sair
            """)
        i = input()
            
        if i == "1":
            startJogo()
            
        elif i == "2":
            print("Saindo do jogo...")
            
        else:
            print("Comando inválido")

# SELECIONAR CLASSE DO PERSONAGEM:
def selecionarClasse():
    global personagemClasse
    print("""
    Selecione sua classe:
        1 - Humano      2 - Capivara

    """)
    personagemClasse = input()
        
    if personagemClasse == "1":
        print("Você selecionou a classe Humano.")

    elif personagemClasse == "2":
        print("Você selecionou a classe Capivara.")

# ESCOLHER OPÇÃO BATALHA:
def opcaoBatalha():
    print("""
1 - ATACAR      2 - USAR ITEM       3 - FUGIR
""")
    
    i = input()

    if i == "1" or i == "2" or i == "3":
        return i
    
    else:
        print("Opção inválida...")
        opcaoBatalha()
    
# BATALHA HUMANO CONTRA CAPIVARA:
def batalhaHumano():
    jogadorEscolha = "0"
    print("Você encontra uma Capivara Selvagem, o que você faz?")
    jogadorEscolha = opcaoBatalha()
    print(f"A escolha do jogador foi {jogadorEscolha}")

# COMEÇAR O JOGO:
def startJogo():
    selecionarClasse()
    
    if personagemClasse == "1":
        batalhaHumano()
    
    elif personagemClasse == "2":
        batalhaCapivara()

    else:
        print("Opção inválida...")
        selecionarClasse()

# MAIN():       
menu()