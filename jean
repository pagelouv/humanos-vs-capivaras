import random
import os

# VARIÁVEIS GLOBAIS: =================================================================================
personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara
personagemVida = 10
inimigoVida = 10
turno = "0" # 0 = seu turno, 1 = turno inimigo
pocaoCura =  1
pocaoDano = 1
danoExtra = "0"

# MENU: =================================================================================
def menu():

    resetGame()

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
        print("------------------------------------------------------------")
        
        i = input("""\n           1- Jogar              2- Sair    
                        """)
            
        if i == "1":
            startJogo()
            
        elif i == "2":
            print("Saindo do jogo...")
            
        else:
            print("Comando inválido")

# RESETAR JOGO: =================================================================================
def resetGame():
    global personagemClasse
    global personagemVida
    global inimigoVida
    global turno      
    global pocaoDano
    global pocaoCura
    global danoExtra 

    personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara
    personagemVida = 10
    inimigoVida = 10
    turno = "0" # 0 = seu turno, 1 = turno inimigo
    pocaoCura =  1
    pocaoDano = 1
    danoExtra = "0"

# CHECAR GAME OVER: =================================================================================
def gameOverCheck():
    global personagemVida

    if personagemVida <= 0:
        print("GAME OVER! VOCÊ PERDEU!")

# SELECIONAR CLASSE DO PERSONAGEM: =================================================================================
def selecionarClasse():
    global personagemClasse
    personagemClasse = input("""
     -------------------CHOOSE YOUR DESTINY---------------------
          
                     1 - Humano      2 - Capivara

                                 """)
        
    if personagemClasse == "1":
        os.system('cls')
        print("Você selecionou a classe Humano.")

    elif personagemClasse == "2":
        print("Você selecionou a classe Capivara.")

# ESCOLHER OPÇÃO BATALHA: =================================================================================
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

# TURNO INIMIGO:  =================================================================================
def turnoInimigo():

    global personagemVida
    global personagemClasse

    ataqueInimigo = random.randint(0, 19)
    print(f"d20 inimigo: {ataqueInimigo}")

    if ataqueInimigo >= 9 and ataqueInimigo <= 18:    # SE O INIMIGO ACERTAR:
        if personagemClasse == "1":                    # VERSÃO HUMANO:
            print("A Capivara tenta te atacar...")
            print("A Capivara te acerta!")
            print("\n_/﹋\_")
            print("(҂´.`")
            print("<¨¨¨|")
            print("\nVocê tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        if personagemClasse == "2":                  # VERSÃO CAPIVARA:
            print("O humano tenta atirar em você!")
            print("O humano te acerta!")
            print("Você tomou 1 de dano!")
            print(" /\_/")  
            print("( x.x )")
            print(" > 0 <")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")
    
    if ataqueInimigo >= 0 and ataqueInimigo <= 8:
        if personagemClasse == "1":
            print("A Capivara tenta te atacar...")
            print("Você dá uma cambalhota por cima do ataque dela! Ela erra!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            gameOverCheck()
            input("Pressione para continuar...")

        if personagemClasse == "2":
            print("O humano tenta atirar em você!")
            print("Com seu poder de Capivara Matrix você desvia!")
            print("\n /\_/")  
            print("( `.´ )")
            print(" > M <")
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")
    
    if ataqueInimigo == 19:
        if personagemClasse == "1":
            print("A Capivara lança um raio lazer em você!")
            print("Ela da um acerto crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        if personagemClasse == "2":
            print("O humano é um Jedi!")
            print("Ele usa a força para te prender na parede! Dano crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")


# ATACAR:  =================================================================================
def atacar():

    global inimigoVida
    global turno
    global danoExtra

    os.system('cls') # LIMPA TELA

    input("Pressione para jogar o d20...")
    tiro = random.randint(0, 20) 
    print(f"Jogando dado d20: {tiro}")

    if tiro >= 11 and tiro <= 19:
        print("Você acerta!")
        dano = random.randint(1, 2)
        print("Toma! Bem no alvo")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print(f"Você deu {dano} de dano!")
        inimigoVida = inimigoVida - dano
        
    elif tiro >= 0 and tiro <= 10:
        print("Você errou!")
        print("\n_/﹋\_")
        print("(҂´.`")
        print("<¨¨¨|")

    elif tiro == 20:
        print("Dano crítico!")

        dano = 3
        print("\nToma! Headshot!")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print(f"\nVocê deu {dano} de dano! Insano!")
        inimigoVida = inimigoVida - dano
    
    verificarDanoExtra()

    print(f"Sua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida}")
    print("")
    input("Pressione para continuar...")

    danoExtra = "0"

#ATAQUE DA CAPIVARA =======================================================================
def ataque():

    global inimigoVida
    global turno
    global danoExtra

    os.system('cls') # LIMPA TELA

    input("Pressione para jogar o d20...")
    tiro = random.randint(0, 20) 
    print(f"Jogando dado d20: {tiro}")

    if tiro >= 11 and tiro <= 19:
        print("Você acerta!")
        dano = random.randint(1, 2)
        print("Mordida no braço")
        print("\n /\_/")  
        print("( `.´ )")
        print(" > M <") 
        print(f"Você deu {dano} de dano!")
        inimigoVida = inimigoVida - dano
    
        
    elif tiro >= 0 and tiro <= 10:
        print("Você errou!")
        print("\n /\_/")  
        print("( x.x )")
        print(" > w <") 
       

    elif tiro == 20:
        print("Dano crítico!")

        dano = 3
        print("\nMordida no Pescoço!")
        print("\n /\_/")  
        print("( `.´ )")
        print(" > M <") 
        print(f"\nVocê deu {dano} de dano! Insano!")
        inimigoVida = inimigoVida - dano
    
    verificarDanoExtra()

    print(f"Sua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida}")
    print("")
    input("Pressione para continuar...")

    danoExtra = "0"
# FUGIR:  ==================================================================================================
def fugir():
    os.system('cls')
    if personagemClasse == "1":
        print("Você tem certeza que quer fugir?")
        i = input("1- Sim      2- Não")
        print("")
        if i == "1":
            print("Sério mesmo que você vai fugir? É só uma capivara cara...")
            print("")
            x = input("1- Sim estou com muito medo de uma capivarinha...    2- Não")
            print("")
            if x == "1":
                print("Sério mesmo? Eu nunca vi um humano tentando fugir com medo de uma capivara... Essa é nova")
                print("")
                y = input("1- Eu sou um covarde          2- Eu sou um covarde")
                if y == "1":
                    quit()
                else:
                    quit()
            elif x == "2":
                os.system('cls') 
                batalhaHumano()
            else:
                os.system('cls') 
                print("Não sabe nem digita")   
                quit()
        else:
            os.system('cls') 
            batalhaHumano()
    
    elif personagemClasse == "2":
        print("Você tem certeza que quer fugir?")
        i = input("1- Sim      2- Não")
        print("")
        if i == "1":
            print("Tá tudo bem... humanos são malvados não tem problema fugir!")
            quit()
        
        if i == "2":
            batalhaCapivara()

# USAR ITEM: =============================================================================================
def usarItem():
    
    global pocaoCura
    global pocaoDano
    global personagemVida
    global danoExtra

    os.system('cls')
    print("=============== INVENTÁRIO ===============")
    print(f"1- Paçoca Encantada (+2HP): {pocaoCura}")
    print(f"2- Chumbinho de Festa Junina (+2 Dano Garantido): {pocaoDano}")

    print("")
    print("Selecione uma opção...")
    i = input()

    if i == "1" and pocaoCura == 1:
        print("Você usou uma Poção de Cura!")
        personagemVida = personagemVida + 2
        pocaoCura = pocaoCura - 1

        print(f"Sua vida agora é: {personagemVida} HP")
    
    elif i == "1" and pocaoCura == 0:
        print("Você não possui mais deste item!")
        input("Pressione para continuar...")
        usarItem()

    elif i == "2" and pocaoDano == 1:
        print("Você usou um item de dano extra! Será aplicado o dano no seu próximo turno!")
        danoExtra = "1"
        pocaoDano = pocaoDano - 1
    
    elif i == "2" and pocaoDano == 0:
        print("Você não possui mais deste item!")
        input("Pressione para continuar...")
        usarItem()


# VERIFICAR DANO EXTRA: =================================================================================
def verificarDanoExtra():

    global danoExtra
    global inimigoVida

    if danoExtra == "1":
        print("Você deu Dano Extra! O Inimigo toma 2 de dano!")
        inimigoVida = inimigoVida - 2


# BATALHA HUMANO CONTRA CAPIVARA: =================================================================================
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
                batalhaHumano()

            turno = "1"

        if turno == "1":
            print("\n\nTurno inimigo!")
            print("")
            turnoInimigo()
            turno = "0"

def batalhaCapivara():


    global turno
    global personagemVida
    global inimigoVida

    while personagemVida > 0 and inimigoVida > 0:
            
        if turno == "0":
            print("\nVocê encontra um humano armado, o que você faz?")
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"\nSua escolha foi:  {jogadorEscolha}")

            if jogadorEscolha == "1":
                ataque()
            
            elif jogadorEscolha == "2":
                usarItem()
            
            elif jogadorEscolha == "3":
                fugir()
            
            else:
                print("Opção inválida...")
                batalhaCapivara()

            turno = "1"

        if turno == "1":
            print("\n\nTurno inimigo!")
            print("")
            turnoInimigo()
            turno = "0"


# COMEÇAR O JOGO: =================================================================================
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
