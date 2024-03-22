import random
import os

# VARIÁVEIS GLOBAIS:
personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara
personagemVida = 10
inimigoVida = 10
turno = "0" # 0 = seu turno, 1 = turno inimigo

# MENU:
def menu():
    i = "0"

    while i != "2":
        print("-----------------------------------------------------------" )
        print("-----------------------------------------------------------" )
        print("-----------------------------------------------------------" )
        print("-----------------------------------------------------------" )
        print("------------------HUMAN  X  CAPIVARA-----------------------" )
        print("_/﹋\_-----------------------------------------------------" )
        print("(҂`_´)--------------------------------------^..^____/------" )
        print("<;︻╦╤─ *-*-*-*-*-*-*-*-*-*------------------\./ ___)------" )
        print("-----------------------------------------------||  || -----" )
        print("           1- Jogar              2- Sair")
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

# TURNO INIMIGO
def turnoInimigo():

    global personagemVida
    global personagemClasse

    ataqueInimigo = random.randint(0, 5)
    print(f"d20 inimigo: {ataqueInimigo}")

    if ataqueInimigo >= 0 and ataqueInimigo <= 2:    # SE O INIMIGO ACERTAR:
        if personagemClasse == "1":                    # VERSÃO HUMANO:
            print("A Capivara tenta te atacar...")
            print("A Capivara te acerta!")
            print("Você tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")

        elif personagemClasse == "2":                  # VERSÃO CAPIVARA:
            print("O humano tenta atirar em você!")
            print("O humano te acerta!")
            print("Você tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
    
    if ataqueInimigo >= 3 and ataqueInimigo <= 4:
        if personagemClasse == "1":
            print("A Capivara tenta te atacar...")
            print("Você dá uma cambalhota por cima do ataque dela! Ela erra!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")

        elif personagemClasse == "2":
            print("O humano tenta atirar em você!")
            print("Com seu poder de Capivara Matrix você desvia!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
    
    if ataqueInimigo == 5:
        if personagemClasse == "1":
            print("A Capivara lança um raio lazer em você!")
            print("Ela da um acerto crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")

        if personagemClasse == "2":
            print("O humano é um Jedi!")
            print("Ele usa a força para te prender na parede! Dano crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")

# ATACAR
def atacar():

    global inimigoVida
    global turno

    os.system('cls') # LIMPA TELA

    tiro = random.randint(0, 20) 
    print(f"Jogando dado d20: {tiro}")

    if tiro >= 11 and tiro <= 19:
        print("Você acerta!")
        dano = random.randint(1, 2)
        print("Toma! Bem no alvo")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print("")
        print(f"Você deu {dano} de dano!")
        inimigoVida = inimigoVida - dano
        print(f"Sua vida: {personagemVida}")
        print(f"Vida inimiga: {inimigoVida}")

        turno = "1"
    
    elif tiro >= 0 and tiro <= 10:
        print("Você errou!")
        print(f"Sua vida: {personagemVida}")
        print(f"Vida inimiga: {inimigoVida}")

        turno = "1"

    elif tiro == 20:
        print("Você critou! Dano crítico!")
        print("")
        dano = 3
        print("Toma! Headshot!")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print("")
        print(f"Você deu {dano} de dano! Insano!")
        inimigoVida = inimigoVida - dano
        print(f"Sua vida: {personagemVida}")
        print(f"Vida inimiga: {inimigoVida}")

        turno = "1"

# BATALHA HUMANO CONTRA CAPIVARA:
def batalhaHumano():

    global turno
    global personagemVida
    global inimigoVida

    while personagemVida > 0 and inimigoVida > 0:
        if turno == "0":
            print("Você encontra uma Capivara Selvagem, o que você faz?")
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"A escolha do jogador foi {jogadorEscolha}")

            if jogadorEscolha == "1":
                atacar()
            
            elif jogadorEscolha == "2":
                usarItem()
            
            elif jogadorEscolha == "3":
                fugir()
            
            else:
                print("Opção inválida...")

        if turno == "1":
            print("")
            print("")
            print("")
            print("Turno inimigo!")
            print("")
            turnoInimigo()
            turno = "0"

# COMEÇAR O JOGO:
def startJogo():

    os.system('cls') # LIMPA TELA

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