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
contarTurno = 0
inimigoVida2 = 15
verificarMorto = "1"

# MENU: =================================================================================
def menu():

    resetGame()

    i = "0"
    os.system('cls')

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

# RESETAR JOGO: =================================================================================
def resetGame():
    global personagemClasse
    global personagemVida
    global inimigoVida
    global turno      
    global pocaoDano
    global pocaoCura
    global danoExtra 
    global contarTurno
    global inimigoVida2
    global verificarMorto

    personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara
    personagemVida = 10
    inimigoVida = 1
    inimigoVida2 = 15
    turno = "0" # 0 = seu turno, 1 = turno inimigo
    pocaoCura =  1
    pocaoDano = 1
    danoExtra = "0"
    contarTurno = 0
    verificarMorto = "1"

# CHECAR GAME OVER: =================================================================================
def gameOverCheck():
    global personagemVida
    global contarTurno

    if personagemVida <= 0:
        print("")
        print("=======================")
        print("GAME OVER! VOCÊ PERDEU!")
        print("=======================")
        print("")
        print(f"Você sobreviveu {contarTurno} turnos!")
        print("")
        input("Pressione para sair...")
        quit()

# SELECIONAR CLASSE DO PERSONAGEM: =================================================================================
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
    global inimigoVida

    ataqueInimigo = random.randint(1, 20)
    print("")
    print(f"d20 inimigo: {ataqueInimigo}")
    print("")

    if ataqueInimigo >= 10 and ataqueInimigo <= 19:    # SE O INIMIGO ACERTAR:
        if personagemClasse == "1":                    # VERSÃO HUMANO:
            print("A Capivara tenta te atacar...")
            print("A Capivara te acerta!")
            print("Você tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        elif personagemClasse == "2":                  # VERSÃO CAPIVARA:
            print("O humano tenta atirar em você!")
            print("O humano te acerta!")
            print("Você tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")
    
    if ataqueInimigo >= 0 and ataqueInimigo <= 9:
        if personagemClasse == "1":
            print("A Capivara tenta te atacar...")
            print("Você dá uma cambalhota por cima do ataque dela! Ela erra!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        elif personagemClasse == "2":
            print("O humano tenta atirar em você!")
            print("Com seu poder de Capivara Matrix você desvia!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")
    
    if ataqueInimigo == 20:
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

# TURNO  SEGUNDO INIMIGO:  =================================================================================
def turnoSegundoInimigo():

    global personagemVida
    global personagemClasse
    global inimigoVida2

    ataqueInimigo = random.randint(1, 20)
    print("")
    print(f"d20 inimigo: {ataqueInimigo}")
    print("")

    if ataqueInimigo >= 10 and ataqueInimigo <= 19:    # SE O SEGUNDO INIMIGO ACERTAR:
        if personagemClasse == "1":                    # VERSÃO HUMANO:
            print("A Capivara Mãe tenta te atacar...")
            print("A Capivara te acerta!")
            print("Você tomou 2 de dano!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        elif personagemClasse == "2":                  # VERSÃO CAPIVARA:
            print("O humano tenta atirar em você!")
            print("O humano te acerta!")
            print("Você tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")
    
    if ataqueInimigo >= 0 and ataqueInimigo <= 9:
        if personagemClasse == "1":
            print("A Capivara Mãe tenta te atacar...")
            print("Você dá uma cambalhota por cima do ataque dela! Ela erra!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        elif personagemClasse == "2":
            print("O humano tenta atirar em você!")
            print("Com seu poder de Capivara Matrix você desvia!")
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")
    
    if ataqueInimigo == 20:
        if personagemClasse == "1":
            print("A Capivara Mãe lança um raio lazer em você!")
            print("Ela da um acerto crítico! -4 de vida!")
            personagemVida = personagemVida - 4
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

        if personagemClasse == "2":
            print("O humano é um Jedi!")
            print("Ele usa a força para te prender na parede! Dano crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            print("")
            gameOverCheck()
            input("Pressione para continuar...")

# ATACAR:  =================================================================================
def atacar(): # HUMANO ATACA CAPIVARA 1

    global inimigoVida
    global turno
    global danoExtra

    os.system('cls') # LIMPA TELA

    input("Pressione para jogar o d20...")
    print("")
    tiro = random.randint(0, 20) 
    print(f"Jogando dado d20: {tiro}")
    print("")

    if tiro >= 11 and tiro <= 19:
        print("Você acerta!")
        dano = random.randint(1, 3)
        print("Toma! Bem no alvo")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print("")
        print(f"Você deu {dano} de dano!")
        inimigoVida = inimigoVida - dano
        
    elif tiro >= 0 and tiro <= 10:
        print("Você errou!")

    elif tiro == 20:
        print("Você critou! Dano crítico!")
        print("")
        dano = 5
        print("Toma! Headshot!")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print("")
        print(f"Você deu {dano} de dano! Insano!")
        inimigoVida = inimigoVida - dano
    
    verificarDanoExtra()

    print(f"Sua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida}")
    print("")
    input("Pressione para continuar...")

    danoExtra = "0"

# ATACAR SEGUNDO INIMIGO:  =================================================================================
def atacarSegundoInimigo(): # HUMANO ATACA CAPIVARA MAE

    global inimigoVida2
    global turno
    global danoExtra

    os.system('cls') # LIMPA TELA

    input("Pressione para jogar o d20...")
    print("")
    tiro = random.randint(0, 20) 
    print(f"Jogando dado d20: {tiro}")
    print("")

    if tiro >= 11 and tiro <= 19:
        print("Você acerta!")
        dano = random.randint(1, 3)
        print("Toma! Bem no alvo")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print("")
        print(f"Você deu {dano} de dano!")
        inimigoVida2 = inimigoVida2 - dano
        
    elif tiro >= 0 and tiro <= 10:
        print("Você errou!")

    elif tiro == 20:
        print("Você critou! Dano crítico!")
        print("")
        dano = 5
        print("Toma! Headshot!")
        print("_/﹋\_")
        print("(҂`_´")
        print("<;︻╦╤─") 
        print("")
        print(f"Você deu {dano} de dano! Insano!")
        inimigoVida2 = inimigoVida2 - dano
    
    verificarDanoExtra()

    print(f"Sua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida2}")
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
                print("Não sabe nem digitar!")   
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
        
        elif i == "2":
            batalhaCapivara()

# USAR ITEM: =============================================================================================
def usarItem():
    
    global pocaoCura
    global pocaoDano
    global personagemVida
    global danoExtra

    os.system('cls')
    print("=============== INVENTÁRIO ===============")
    print("")
    print(f"1- Paçoca Encantada (+2HP): {pocaoCura}")
    print(f"2- Chumbinho de Festa Junina (+2 Dano Garantido): {pocaoDano}")
    print("3- Voltar...")
    print("")
    print("==========================================")
    print("")
    print("Selecione uma opção...")
    i = input()

    if i == "1" and pocaoCura >= 1:
        print("Você usou uma Poção de Cura!")
        personagemVida = personagemVida + 2
        pocaoCura = pocaoCura - 1
        print(f"Sua vida agora é: {personagemVida} HP")
        input("Pressione para continuar...")
    
    elif i == "1" and pocaoCura == 0:
        print("Você não possui mais deste item!")
        input("Pressione para continuar...")
        usarItem()

    elif i == "2" and pocaoDano >= 1:
        print("Você usou um item de dano extra! Será aplicado o dano no seu próximo turno!")
        input("Pressione para continuar...")
        danoExtra = "1"
        pocaoDano = pocaoDano - 1
    
    elif i == "2" and pocaoDano == 0:
        print("Você não possui mais deste item!")
        input("Pressione para continuar...")
        usarItem()
    
    elif i == "3":
        batalhaHumano()

    else:
        usarItem()


# VERIFICAR DANO EXTRA: =================================================================================
def verificarDanoExtra():

    global danoExtra
    global inimigoVida
    global inimigoVida2

    if danoExtra == "1" and inimigoVida > 0:
        print("Você deu Dano Extra! O Inimigo toma 2 de dano!")
        inimigoVida = inimigoVida - 2
    
    elif danoExtra == "1" and inimigoVida <= 0 and inimigoVida2 > 0:
        print("Você deu Dano Extra! O Inimigo toma 2 de dano!")
        inimigoVida2 = inimigoVida2 - 2
 

# BATALHA HUMANO CONTRA CAPIVARA: =================================================================================
def batalhaHumano():

    global turno
    global personagemVida
    global inimigoVida
    global inimigoVida2
    global contarTurno
    global pocaoCura
    global pocaoDano
    global verificarMorto

    while personagemVida > 0 and inimigoVida > 0:

        os.system('cls')

        if turno == "0":
            print(f"Sua vida: {personagemVida}     Vida inimiga: {inimigoVida}")
            print("")
            print("Você encontra uma Capivara Selvagem, o que você faz?")
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"A escolha do jogador foi {jogadorEscolha}")

            if jogadorEscolha == "1":
                atacar()
            
            elif jogadorEscolha == "2":
                usarItem()
                batalhaHumano()
            
            elif jogadorEscolha == "3":
                fugir()
            
            else:
                print("Opção inválida...")
                batalhaHumano()

            turno = "1"

        if turno == "1" and inimigoVida > 0:
            print("")
            print("==============")
            print("Turno inimigo!")
            print("==============")
            turnoInimigo()
            turno = "0"
        
        contarTurno = contarTurno + 1
    
    # JOGADOR DERROTA PRIMEIRO INIMIGO, SEGUNDO INIMIGO:
    if inimigoVida <= 0 and verificarMorto == "1":
        os.system('cls')
        print("")
        print("Parabéns! Você derrotou a capivara bebê!")
        print("")
        print("========== LOOT ==========")     # JOGADOR RECEBE LOOT
        print("")
        print("+2 Paçocas Encantadas!")
        print("+1 Chumbinho de Festa Junina!")
        print("")
        print("==========================")
        pocaoCura = pocaoCura + 2
        pocaoDano = pocaoDano + 1

        print("")
        input("...")
        print("")
        print("A Capivara bebê chora por sua mãe!")
        input("...")
        print("")
        print("A Capivara Mãe vê você atacando a filha dela!")
        input("...")
        print("")
        print("A Capivara Mãe se junta a batalha!")
        input("...")
        print("")

        verificarMorto = "0"

    turno = "0"     # TURNO VIRA DO JOGADOR

    while personagemVida > 0 and inimigoVida <= 0 and inimigoVida2 > 0:      # BATALHA JOGADOR CONTRA SEGUNDO INIMIGO:
        os.system('cls')

        if turno == "0":
            print(f"Sua vida: {personagemVida}     Vida inimiga: {inimigoVida2}")
            print("")
            print("Você se depara com a Capivara Mãe, o que você faz?")
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"A escolha do jogador foi {jogadorEscolha}")

            if jogadorEscolha == "1":
                atacarSegundoInimigo()
            
            elif jogadorEscolha == "2":
                usarItem()
                batalhaHumano()
            
            elif jogadorEscolha == "3":
                fugir()
            
            else:
                print("Opção inválida...")
                batalhaHumano()

            turno = "1"

        if turno == "1" and inimigoVida2 > 0:
            print("")
            print("==============")
            print("Turno inimigo!")
            print("==============")
            turnoSegundoInimigo()
            turno = "0"
        
        contarTurno = contarTurno + 1


    
    print(f"Total de turnos: {contarTurno}")

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