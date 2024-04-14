import random
import os
import sys
import time
import anima as an


# VARIÁVEIS GLOBAIS: =================================================================================

personagemClasse = "0" #0 = nenhuma, 1 = humano, 2 = capivara
personagemVida = 50
inimigoVida = 50
turno = "0" # 0 = seu turno, 1 = turno inimigo
pocaoCura =  1
pocaoDano = 1
danoExtra = "0"
contarTurno = 0
inimigoVida2 = 55
verificarMorto = "1"
RED = '\033[91m'
RESET = '\033[0m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
DKG = '\033[1;32m'
BLUE = '\033[94m'
BLACK = "\033[1;30m"
WHITE = "\033[1;37m"
TITULO =f"""\n
    {RED} __                                                   {WHITE} ___ ___  _______ {RED}                       __                                   
    {RED}|  |--..--.--..--------..---.-..-----..-----..-----.  {WHITE}|   Y   ||   _   |{RED}  .----..---.-..-----.|__|.--.--..---.-..----..---.-..-----.
    {RED}|     ||  |  ||        ||  _  ||     ||  _  ||__ --|  {WHITE}|.  |   ||   1___|{RED}  |  __||  _  ||  _  ||  ||  |  ||  _  ||   _||  _  ||__ --|
    {RED}|__|__||_____||__|__|__||___._||__|__||_____||_____|  {WHITE}|.  |   ||____   |{RED}  |____||___._||   __||__| \___/ |___._||__|  |___._||_____|
                                                          {WHITE}|:  1   ||:  1   |     {RED}          |__|                                         
                                                          {WHITE} \:.. ./ |::.. . |                                                            
                                                          {WHITE}  `---'  `-------' {RESET}"""
texto = RED +"""
        Numa manhã ensolarada numa pequena cidade às margens de um rio, um estranho acontecimento começou a se desenrolar.

        Um grupo de capivaras, decidiu tomar posse das terras próximas ao rio, que há muito tempo pertenciam aos moradores

        Os moradores, inicialmente surpresos com a audácia das capivaras, logo se viram em uma batalha inesperada
        pela terra. 
        Armados com enxadas e qualquer coisa que pudessem encontrar, os moradores se prepararam para defender o que era deles.

        As capivaras, com suas afiadas garras e dentes, estavam determinadas a manter o que consideravam seu território agora.

        
                                             DE QUAL LADO VOCÊ VAI FICAR?? 
""" + RESET
texto1 =f"""{RED}
                        Ora, ora, ora! o que temos aqui?
                    Parece que uma capivara se perdeu do grupo!
                        acho que vai dar um ótimo troféu!
                          
                          PREPARE-SE PARA A MORTE!!! 
{RESET}""" 
texto2 =f"""{RED}
                        Quando esses HUMANOS irão mandar
                    alguem que não seja um fracote como você?

                        VAMOS ACABAR LOGO COM ISSO!!
{RESET}"""
texto3 =f"""
                         ISSO NÂO VAI FICAR ASSIM!!!
                     ALGUMA CAPIVARA MAIS FORTE ME VINGARÁ!
"""
texto4 = """
                        ESTAVAMOS EM PAZ ATÉ VOCÊ APARECER!
                        
                    PREPARE-SE PARA SENTIR MUITA, MAS MUITA DOR!
"""
velo = 0.0

# MENU: =================================================================================
def menu():

    resetGame()

    i = "0"
    os.system('cls')

    while i != "2":
        
       
        print("""\n
 __| |________________________________________________________________________________________________________________________| |__
(__   ________________________________________________________________________________________________________________________   __)
   | |                                                                                                                        | |""")
        ler_texto()
        print("""
 __| |________________________________________________________________________________________________________________________| |__
(__   ________________________________________________________________________________________________________________________   __)
   | |                                                                                                                        | |""")
        input("...")
        os.system('cls')
        titulo()
        print(F"""{DKG}
                                  ____________________________________________________________________
                                  |###################################################################|            
                                  |###################################################################|
                                  |###|-----------------------------------------------------------|###|
                                  |###|-----------------------------------------------------------|###|
                                  |###|--_/﹋\_-------------------------------------- /\_/ -------|###|
                                  |###|--(҂`_´)--------------------------------------( `.´ )------|###|
                                  |###|--<;︻╦╤─ *-*-*-*-*-*-*-*-*-*------------------\ m /-------|###|
                                  |###|------------------------------------------------\./--------|###|
                                  |###|-----------------------------------------------------------|###|
                                  |###|                                                           |###|
                                  |###|-----------------------------------------------------------|###|
                                  |###################################################################|
                                  |###########                                           #############|
                                  |                1 - JOGAR  2 - INSTRUÇÕES  3 - SAIR                |
                                  |___________________________________________________________________|{RESET}""")
    
       


        i = input("\n                                                                  ")

        if i == "1":
            os.system('cls')
            startJogo()
            

        elif i == "2":
            print("Saindo do jogo...")

        else:
            os.system('cls')
            print("Comando inválido")
            
 # HISTÓRIA ==============================================================================
def ler_texto():
    global texto
    
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velo)

    

    print()
def titulo():
    global TITULO


    for letra in TITULO:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velo)

    print()

 # HISTORIA 2 ============================================================================
def ler_texto1():
    global texto1


    for letra in texto1:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velo)

    print()
 # HISTORIA 2.2 =========================================================================
def ler_texto2():
    global texto2

    for letra in texto2:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velo)
    print()    
 #HISTORIA VIRADA HUMANO VS CAPIVARA ===============================================================
def ler_texto3():
    global texto3

    for letra in texto3:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velo)
    print()       
def ler_texto4():
    global texto4

    for letra in texto4:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velo)
    print()

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
    inimigoVida = 10
    inimigoVida2 = 10
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
    global personagemClasse

    if personagemVida <= 0:
        if personagemClasse =="2":
            os.system('cls')
            print(f"""{DKG} 
                             __{BLACK} ..--''``---....___   _..._    {DKG}__
                      /// //{BLACK}_.-'    .-/";  `        ``<._  ``.''_ `.{DKG} / // /
                    ///{BLACK}_.-' _..--.'X    \                    |{DKG} // //
                    / {BLACK}(_..-' {DKG}//{BLACK} (<      ;_..__               ;{DKG} `' / ///
                    / // // //  {BLACK}`-X._,_)' // / ``--...____..-'{DKG} /// / //

                                            
            {RED} __   __ _  _ __  ___   _   _    ___  __ _  _ __  _ __    ___ 
             \ \ / /| || '__|/ _ \ | | | |  / __|/ _` || '__|| '_ \  / _ *
              \ V / | || |  | (_) || |_| | | (__| (_| || |   | | | ||  __/
               \_/  |_||_|   \___/  \__,_|  \___|\__,_||_|   |_| |_| \___|
  
  
{RESET}""")
        else:
        
             print(f"""                     ______________________
         ____,      /,  MALDITAS CAPIVARAS )
       __)____)__  //  *------------------*              
         / # o    //             {RED}       ______     ______     __    __     ______     {RESET}
         \,__>                   {RED}      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\.   {RESET}
      .o-'-'--._                 {RED}      \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\    {RESET}
     / |\_      '.               {RED}       \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\. {RESET}
    |  |  \   -,  \              {RED}        \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/  {RESET}
    \  /   \__| ) |              {RED}           ______     __   __   ______     ______    {RESET}
     '|_____[)) |,/              {RED}          /\  __ \   /\ \ / /  /\  ___\   /\  == \.  {RESET}
        |===H=|\ >>              {RED}          \ \ \/\ \  \ \ \./   \ \  __\   \ \  __<   {RESET}
        \  __,| \_\.             {RED}           \ \_____\  \ \__|    \ \_____\  \ \_\ \_\.{RESET}
         \/   \  \_\.            {RED}            \/_____/   \/_/      \/_____/   \/_/ /_/ {RESET}
         |\    |  \/
         | \   \   \\
         |  \   |   \\
         |__|\ ,-ooD \\
         |--\_(\.-'   \o
         '-.__)



""")
             print(f"Você sobreviveu {contarTurno} turnos!")
             print("")
             input("Pressione para sair...")
             quit()

# SELECIONAR CLASSE DO PERSONAGEM: =================================================================================
def selecionarClasse():
    
    global personagemClasse

    print(YELLOW +"""
 ____ __  __  _____   _____    __ _____    _  _  _____  __ __ _____    _____ _____   __ _____ __ __  __ _  _ 
((    ||==|| ((   )) ((   ))  ((  ||==      \// ((   )) || || ||_//    ||  ) ||==   ((   ||   || ||\ ||  \// 
 .\__ ||  ||   \_//    \_//  \_)) ||___  _  //    \_//   \_// || \   _ ||_// ||___ \_))  ||   || || \||  //  

""" + RESET)

    print(f"""
        ╔═════════════════════════════╗  {RED}  __                ___ {RESET}   ╔═════════════════════════════╗  
        ║                             ║  {RED} /_ |              |__ \ {RESET}  ║                             ║
        ║=========={BLACK}\///////\{RESET}          ║  {RED}  | |     _____       ) | {RESET} ║============|\_/|=           ║
        ║          {WHITE}| _   _ |{RESET}          ║  {RED}  | |    |_____|     / /  {RESET} ║##########=( o"O )=          ║
        ║========={WHITE}( ({BLUE}o{WHITE}) ({BLUE}o{WHITE}) ){RESET}=========║  {RED}  | |               / /_  {RESET} ║===========/\ " /\===========║
        ║          {WHITE}|  . .  |{RESET}          ║  {RED}  |_|              |____| {RESET} ║         =| |\_/| |=#########║
        ║           {WHITE}\  _  /{RESET}===========║                             ║         =\_>---<_/==========║
        ║            {WHITE}\___/{RESET}            ║                             ║          (___|___)          ║
        ╚═════════════════════════════╝                             ╚═════════════════════════════╝ 
                    HUMANO                                                      CAPIVARA
""")

    
   
    personagemClasse = input("                                                     ")

    if personagemClasse == "1":
        os.system('cls')
        print(f"""{GREEN}
                     ╔═════════════════════════════════════════════════╗
                     ║[0]{WHITE}                     ______                {GREEN}[0]║═══════════════════════════════════════════════════════╗
                     ║ |{WHITE}                     <((((((\.\.             {GREEN}| ║  =====================================================║
                     ║ |{WHITE}                     /      . ]\.            {GREEN}| ║   {RED}.__ {GREEN}                                       =========║    
                     ║ |{WHITE}                     ;--..--._|]             {GREEN}| ║   {RED}|  |__   __ __   _____  _____     ____    ____{GREEN} =====║
                     ║ |{WHITE} (.\                 '--/\--'  )             {GREEN}| ║   {RED}|  |  \ |  |  \ /     \ \__  \   /    \  /  _ \.{GREEN}====║
                     ║ |{WHITE}  \.\                | '-'    |              {GREEN}| ║   {RED}|   Y  \|  |  /|  Y Y  \ / __ \_|   |  \(  <_> ){GREEN}====║
                     ║ |{WHITE}   \.\               . -==- .-|              {GREEN}| ║   {RED}|___|  /|____/ |__|_|  /(____  /|___|  / \____/{GREEN}=====║
                     ║ |{WHITE}    \.\               \.__.'   \--._         {GREEN}| ║        {RED}\/              \/      \/      \/ {GREEN}============║      
                     ║ |{WHITE}    [\.\          __.--|       //  _/'--.    {GREEN}| ║ ======================================================║
                     ║ |{WHITE}    \ \.\       .'-._ ('-----'/ __/      \.  {GREEN}| ║═══════════════════════════════════════════════════════╝ 
                     ║ |{WHITE}     \ \.\     /   __>|      | '--.       |  {GREEN}| ║          ║ |       
                     ║ |{WHITE}      \ \.\   /   \   |     /    /       /   {GREEN}| ║          ║ |{WHITE} VIDA :{BLUE} ▄▄▄▄▄▄▄▄▄▄▄{GREEN}
                     ║ |{WHITE}        \ '\ /     \  |     |  _/       /    {GREEN}| ║          ║ |{WHITE} FORÇA:{BLUE} ▄▄▄▄▄▄▄▄▄▄{GREEN}
                     ║ |{WHITE}         \  \       \ |     | /        /     {GREEN}| ║          ║ |{WHITE} ARMAS:{BLUE} ▄▄▄▄▄▄▄▄▄▄{GREEN}       ____  
                     ║ |{WHITE}          \  \       \        /              {GREEN}| ║          ╚══════════════════════════|____|
                     ║[0]{WHITE}                                           {GREEN}[0]║                                     
                     ╚═════════════════════════════════════════════════╝ 
              {RESET}""")
        input("Press...")
        os.system('cls')
        print(f"""{GREEN}      
                     ╔════════════════════════════════════╗
                     ║[0]                              [0]║
                     ║ |                                | ║ 
                     ║ |{WHITE}             ___                {GREEN}| ║
                     ║ |{WHITE}          .="   "=._.---.       {GREEN}| ║
                     ║ |{WHITE}        ."         c ` Y´`p     {GREEN}| ║
                     ║ |{WHITE}       /   ,       `. \m/       {GREEN}| ║
                     ║ |{WHITE}      |   '-.   /     /         {GREEN}| ║ 
                     ║ |{WHITE}     _|      )_-\ \_=.\         {GREEN}| ║
                     ║ |{WHITE}   .-'`------)))`=-'"`'"        {GREEN}| ║
                     ║ |                                | ║               
                     ║[0]                              [0]║               
                     ╚════════════════════════════════════╝{RESET}""")
        ler_texto2()
        input("Press...")      

    elif personagemClasse == "2":
        os.system('cls')
        print(f"""{YELLOW}      
                     ╔════════════════════════════════════╗
                     ║[0]                              [0]║
                     ║ |                                | ║════════════════════════════════════════════════════════════════╗  
                     ║ |                                | ║  ========================={GREEN}.__{YELLOW}    ==============================║  
                     ║ |                                | ║   {GREEN}  ____  _____   ______  |__|___  _______   _______ _____ {YELLOW}    ║
                     ║ |{WHITE}             ___                {YELLOW}| ║{GREEN}   _/ ___\ \__  \  \____ \ |  |\  \/ /\__  \  \_  __ \.__  \.{YELLOW}   ║
                     ║ |{WHITE}          .="   "=._.---.       {YELLOW}| ║{GREEN}   \  \___  / __ \_|  |_> >|  | \   /  / __ \_ |  | \/ / __ \_{YELLOW}  ║
                     ║ |{WHITE}        ."         c ` Y´`p     {YELLOW}| ║{GREEN}    \___  >(____  /|   __/ |__|  \_/  (____  / |__|   (____  /{YELLOW}  ║
                     ║ |{WHITE}       /   ,       `. \m/       {YELLOW}| ║{GREEN}        \/      \/ |__|                    \/              \/{YELLOW}   ║
                     ║ |{WHITE}      |   '-.   /     /         {YELLOW}| ║ ===============================================================║
                     ║ |{WHITE}     _|      )_-\ \_=.\         {YELLOW}| ║════════════════════════════════════════════════════════════════╝ 
                     ║ |{WHITE}   .-'`------)))`=-'"`'"        {YELLOW}| ║                  ║ |
                     ║ |                                | ║                  ║ |{WHITE} VIDA :{BLUE} ▄▄▄▄▄▄▄▄▄▄{YELLOW}
                     ║[0]                              [0]║                  ║ |{WHITE} FORÇA:{BLUE} ▄▄▄▄▄▄▄▄▄{YELLOW}
                     ╚════════════════════════════════════╝                  ║ |{WHITE} GARRA:{BLUE} ▄▄▄▄▄▄▄▄ {YELLOW}        ____ 
                                                                             ╚══════════════════════════|____|
{RESET}""")
        input("Press...")
        
        os.system('cls')
        print(f"""{RED}                 
                ╔═════════════════════════════════════════════════╗
                ║[0]{WHITE}                      ______               {RED}[0]║
                ║ |{WHITE}                     <((((((\.\.             {RED}| ║ 
                ║ |{WHITE}                     /      . ]\.            {RED}| ║  
                ║ |{WHITE}                     ;--..--._|]             {RED}| ║
                ║ |{WHITE} (.\                 '--/\--'  )             {RED}| ║   
                ║ |{WHITE}  \.\                | '-'    |              {RED}| ║   
                ║ |{WHITE}   \.\               . -==- .-|              {RED}| ║
                ║ |{WHITE}    \.\               \.__.'   \--._         {RED}| ║         
                ║ |{WHITE}    [\.\          __.--|       //  _/'--.    {RED}| ║ 
                ║ |{WHITE}    \ \.\       .'-._ ('-----'/ __/      \.  {RED}| ║ 
                ║ |{WHITE}     \ \.\     /   __>|      | '--.       |  {RED}| ║                 
                ║ |{WHITE}      \ \.\   /   \   |     /    /       /   {RED}| ║          
                ║ |{WHITE}        \ '\ /     \  |     |  _/       /    {RED}| ║ 
                ║ |{WHITE}         \  \       \ |     | /        /     {RED}| ║
                ║ |{WHITE}          \  \       \        /              {RED}| ║          
                ║[0]{WHITE}                                           {RED}[0]║                                     
                ╚═════════════════════════════════════════════════╝ {RESET}""")
        ler_texto1()
        input("Press...")

# ESCOLHER OPÇÃO BATALHA: =================================================================================
def opcaoBatalha():
    
    i = input("                                                   ")

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

    if ataqueInimigo >= 10 and ataqueInimigo <= 19:    # SE O INIMIGO ACERTAR:
            
        if personagemClasse == "1": # VERSÃO HUMANO:
            an.iniciar_animacao5()
            print("\nVocê tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            input("\nPressione para continuar...")

        elif personagemClasse == "2":                  # VERSÃO CAPIVARA:
            an.iniciar_animacao()
            print("\nVocê tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            input("\nPressione para continuar...")

    if ataqueInimigo >= 0 and ataqueInimigo <= 9:
        if personagemClasse == "1":
            print("\nMORDIDA DE CAPIVARA")
            print("DEFENDIDO!!!")
            an.iniciar_animacaoG()
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            input("\nPressione para continuar...")

        elif personagemClasse == "2":
            print("\nATAQUE DE TIRO DE RIFLE!")
            an.iniciar_animacaoF()
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            input("\nPressione para continuar...")

    if ataqueInimigo == 20:
        if personagemClasse == "1":
            an.iniciar_animacao5()
            print("\nMORDIDA DE CAPIVARA!")
            print("Ela da um acerto crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            input("\nPressione para continuar...")

        if personagemClasse == "2":
            an.iniciar_animacao()
            print("\nO HUMANO ACERTA UM TIRO!")
            print("VOCÊ LEVOU UM TIRO NA PALETA! -2 de vida!") 
            personagemVida = personagemVida - 2
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida}")
            input("\nPressione para continuar...")

    gameOverCheck()
    vencedor()

# TURNO  SEGUNDO INIMIGO:  =================================================================================
def turnoSegundoInimigo():

    global personagemVida
    global personagemClasse
    global inimigoVida2

    ataqueInimigo = random.randint(1, 20)

    if ataqueInimigo >= 10 and ataqueInimigo <= 19:    # SE O SEGUNDO INIMIGO ACERTAR:
        if personagemClasse == "1":                    # VERSÃO HUMANO:
            print("\nATAQUE DE CAPIVARA!")
            print("MEGA COICE!")
            an.iniciar_animacao5()
            print("\nVocê tomou 2 de dano!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            input("Pressione para continuar...")

        elif personagemClasse == "2":                  # VERSÃO CAPIVARA:
            print("\nATAQUE DE BALAS")
            an.iniciar_animacao()
            print("\nVocê tomou 1 de dano!")
            personagemVida = personagemVida - 1
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            input("Pressione para continuar...")

    if ataqueInimigo >= 0 and ataqueInimigo <= 9:
        if personagemClasse == "1":
            print("\nATAQUE DEFENDIDO")
            an.iniciar_animacaoG()
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            input("Pressione para continuar...")

        elif personagemClasse == "2":
            an.iniciar_animacaoF()
            print("\nATAQUE DEFENDIDO!")
            print(f"\nSua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            input("Pressione para continuar...")

    if ataqueInimigo == 20:
        if personagemClasse == "1":
            an.iniciar_animacao5()
            print("ATAQUE DE GARRAS!")
            print("\nAcerto crítico! -4 de vida!")
            personagemVida = personagemVida - 4
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            input("Pressione para continuar...")

        if personagemClasse == "2":
            an.iniciar_animacao6()
            print("O humano é um Jedi!")
            print("\nDano crítico! -2 de vida!")
            personagemVida = personagemVida - 2
            print(f"Sua vida: {personagemVida}")
            print(f"Vida inimiga: {inimigoVida2}")
            input("Pressione para continuar...")
    
    vencedor()
    gameOverCheck()
    
# ATACAR:  =================================================================================
def atacar(): # HUMANO ATACA CAPIVARA 1

    global inimigoVida
    global turno
    global danoExtra

    os.system('cls') 

    print(f"""{BLACK}
                    ╔══════════════════════════════════════════════════╗
    ╔═════════════  ║              ESCOLHA COMO ATACAR                 ║
    ║{WHITE}  \///////\ {BLACK}   ╠══════════════════════════════════════════════════╣
    ║{WHITE}  | _   _ | {BLACK}       HUMANO: {personagemVida}                    CAPIVARA:{inimigoVida}        
    ║{WHITE} ( (o\ /o) ){BLACK}   ╠════════════════╦════════════════╦════════════════╣  
    ║{WHITE}  |  . .  | {BLACK}   ║{RED}    ____      {BLACK}  ║  {RED}     /| {BLACK}      ║ {RED}   _,________ {BLACK} ║
    ║{WHITE}   \ ■■■ /  {BLACK}   ║{RED}    \  _|__   {BLACK}  ║  {RED}     || {BLACK}      ║ {RED}  _T _==____(){BLACK} ║
    ║{WHITE}    \_▬_/   {BLACK}   ║{RED}   __)|   /   {BLACK}  ║  {RED}   __||_{BLACK}      ║ {RED} /##(_)-'     {BLACK} ║
    ╚══════════════ ║{RED}  (___|  (__  {BLACK}  ║  {RED}   ¯¯||¯{BLACK}      ║ {RED}/##/          {BLACK} ║
                    ║{RED}      (_-___) {BLACK}  ║  {RED}     ¯¯ {BLACK}      ║ {RED}¯¯¯           {BLACK} ║
                    ╠════════════════╬════════════════╬════════════════║
                    ║   1 - CHUTE    ║   2 - FACA     ║    3 - ARMA    ║
                    ╚════════════════╩════════════════╩════════════════╝
{RESET}                        
""")
    escolha = input("                             ")

    if escolha == "1":
        print("\nChute Voador!")
        dano = random.randint(1, 3)
        an.iniciar_animacao9()
        
    elif escolha == "2":
        print("\nFacada no bucho!")
        dano = random.randint(0, 5)
        an.iniciar_animacao6()

    elif escolha == "3":
        print("RAJADA DE BALAS")
        dano = random.randint(0, 7)
        an.iniciar_animacao()

    else:
        print("Você perdeu a chance de atacar!")
        dano = 0

    if dano > 0:
        print(f"\nVocê deu {dano} de dano!")
    
    if dano == 0:
        os.system('cls')
        print("\nVocê errou!")
        print(f"""\n 
                  /---------------
                 / SCAPS        /
        _/﹋\_  /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        (҂´=`                                                              
         |__\                                                                                             
    """)


    inimigoVida -= dano


    verificarDanoExtra()

    print(f"\nSua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida}")
    gameOverCheck()
    vencedor()
    input("Pressione Enter para continuar...")

    danoExtra = "0"

# ATACAR SEGUNDO INIMIGO:  =================================================================================
def atacarSegundoInimigo(): # HUMANO ATACA CAPIVARA MAE

    global inimigoVida2
    global turno
    global danoExtra

    os.system('cls') # LIMPA TELA
    
    print(f"""{BLACK}
                    ╔══════════════════════════════════════════════════╗
    ╔═════════════  ║              ESCOLHA COMO ATACAR                 ║
    ║{WHITE}  \///////\ {BLACK}   ╠══════════════════════════════════════════════════╣
    ║{WHITE}  | _   _ | {BLACK}       HUMANO: {personagemVida}                 2ª CAPIVARA:{inimigoVida2}        
    ║{WHITE} ( (o\ /o) ){BLACK}   ╠════════════════╦════════════════╦════════════════╣  
    ║{WHITE}  |  . .  | {BLACK}   ║{RED}    ____      {BLACK}  ║  {RED}     /| {BLACK}      ║ {RED}   _,________ {BLACK} ║
    ║{WHITE}   \ ■■■ /  {BLACK}   ║{RED}    \  _|__   {BLACK}  ║  {RED}     || {BLACK}      ║ {RED}  _T _==____(){BLACK} ║
    ║{WHITE}    \_▬_/   {BLACK}   ║{RED}   __)|   /   {BLACK}  ║  {RED}   __||_{BLACK}      ║ {RED} /##(_)-'     {BLACK} ║
    ╚══════════════ ║{RED}  (___|  (__  {BLACK}  ║  {RED}   ¯¯||¯{BLACK}      ║ {RED}/##/          {BLACK} ║
                    ║{RED}      (_-___) {BLACK}  ║  {RED}     ¯¯ {BLACK}      ║ {RED}¯¯¯           {BLACK} ║
                    ╠════════════════╬════════════════╬════════════════║
                    ║   1 - CHUTE    ║   2 - FACA     ║    3 - ARMA    ║
                    ╚════════════════╩════════════════╩════════════════╝
{RESET}                        
""")
   
    escolha = input("                                       ")

    if escolha == "1":
        print("\nLOSANGO ABERTO!")
        dano = random.randint(1, 3)
        an.iniciar_animacaoA()
        
    elif escolha == "2":
        print("\nFACADA NA PALETA!")
        dano = random.randint(0, 5)
        an.iniciar_animacaoB()

    elif escolha == "3":
        print("RAJADA DE BALAS")
        dano = random.randint(0, 7)
        an.iniciar_animacao2()
        

    else:
        print("Você perdeu a chance de atacar!")
        dano = 0

    if dano > 0:
        print(f"\nVocê deu {dano} de dano!")
    
    if dano == 0:
        os.system('cls')
        print("\nVOCÊ ERROU")
        print(f""" 
                  /---------------
                 /  OPS!!       /
        _/﹋\_  /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                                                       
        (҂´=`                                                            
         |__\                                                                       
                                                                                        
    """)

    inimigoVida2 -= dano


    verificarDanoExtra()

    print(f"\nSua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida2}")
    gameOverCheck()
    vencedor()
    input("Pressione Enter para continuar...")

    danoExtra = "0"

def ataque(): # CAPIVARA CONTRA HUMANO

    
    global inimigoVida
    global turno
    global danoExtra

    os.system('cls') 

    print(f"""
                    ╔══════════════════════════════════════════════════╗
    ╔═════════════  ║              ESCOLHA COMO ATACAR                 ║
    ║    |\_/|      ╠══════════════════════════════════════════════════╣
    ║   ( o"O )        CAPIVARA: {personagemVida}                    HUMANO:{inimigoVida2}        
    ║   /\ " /\     ╠════════════════╦════════════════╦════════════════╣  
    ║  | |\_/| |    ║                ║     _          ║   .-'V'"'V'-.  ║
    ║  \_>---<_/    ║     /./        ║    //===-      ║    \^     ^/   ║
    ║  (___|___)    ║    /./__       ║   ((==-        ║     \^   ^/    ║
    ╚══════════════ ║   (____)))     ║    .\===-      ║      \^_^/     ║
                    ║                ║                ║       ¯¯¯      ║
                    ╠════════════════╬════════════════╬════════════════║
                    ║   1 - COICE    ║   2 - GARRAS   ║  3 - MORDIDA   ║
                    ╚════════════════╩════════════════╩════════════════╝""")
    
    escolha = input("""\n  Escolha um ataque:
                """)

    if escolha == "1":
        print("\nATAQUE DE COICE!")
        dano = random.randint(1, 3)
        an.iniciar_animacao5()
        
        
    elif escolha == "2":
        print("\nATAQUE DE GARRAS!")
        dano = random.randint(0, 5)
        an.iniciar_animacao8()

    elif escolha == "3":
        print("ATAQUE DE MORDIDA!")
        dano = random.randint(0, 7)
        an.iniciar_animacao7()
    else:
        print("\nVocê perdeu a chance de atacar!")
        dano = 0

    if dano > 0:
        print(f"\nVocê deu {dano} de dano!")
    
    if dano == 0:
        os.system('cls')
        print("Você ERRA!")
        print("\n /\_/.")  
        print("( ´.` )  --> EU ESTAVA BRINCANDO")
        print(" \ w /")
        print("  \./")


    inimigoVida -= dano

    verificarDanoExtra()

    print(f"\nSua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida}")
    print("")
    vencedor()
    gameOverCheck()
    input("Pressione Enter para continuar...")

    danoExtra = "0"

# FUGIR:  ==================================================================================================
def fugir():
    os.system('cls')
    if personagemClasse == "1":
        print("      Você tem certeza que quer fugir?")
        i = input("""\n           1- Sim      2- Não
                    """)
        print("")
        if i == "1":
            print("Sério mesmo que você vai fugir...")
          
            print(f"""{WHITE}
 .--""--.___.._
(  <__>  )     `-.     {RED}______     ______     ______     ______     ______{WHITE}    
|`--..--'|      <|    {RED}/\  ___\   /\  __ \   /\  ___\   /\  __ \   /\  __ *{WHITE}
|       :|       /    {RED}\ \ \____  \ \  __ \  \ \ \__ \  \ \  __ \  \ \ \/\ *{WHITE}
|       :|--""-./      {RED}\ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\{WHITE} 
`.__  __;'              {RED}\/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/{WHITE}
    ""
{RESET}""")
            quit()
           
        else:
            os.system('cls') 
            batalhaHumano()

    elif personagemClasse == "2":
        print("Você tem certeza que quer fugir?")
        i = input("1- Sim      2- Não")
        print("")
        if i == "1":
            print(f"""{WHITE}
 .--""--.___.._
(  <__>  )     `-.     {RED}______     ______     ______     ______     ______{WHITE}    
|`--..--'|      <|    {RED}/\  ___\   /\  __ \   /\  ___\   /\  __ \   /\  __ *{WHITE}
|       :|       /    {RED}\ \ \____  \ \  __ \  \ \ \__ \  \ \  __ \  \ \ \/\ *{WHITE}
|       :|--""-./      {RED}\ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\{WHITE} 
`.__  __;'              {RED}\/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/{WHITE}
    ""
{RESET}""")
            quit()

        elif i == "2":
            batalhaCapivara()

# USAR ITEM: =============================================================================================
def ItemCapivara():

    global pocaoCura
    global pocaoDano
    global personagemVida
    global danoExtra

    os.system('cls')
    print(f"""
  _____________________________________
 /                                     \  ════════════════════════════════════════════════╗
|    ╔═════════════════════════════╗    |  ___                      _    __       _        ══
|    ║                             ║    | |_ _|_ ____   _____ _ __ | |_ /_/_ _ __(_) ___   ═══
|    ║============|\_/|=           ║    |  | || '_ \ \ / / _ \ '_ \| __/ _` | '__| |/ _ \. ════
|    ║##########=( o"O )=          ║    |  | || | | \ V /  __/ | | | || (_| | |  | | (_) | ════
|    ║===========/\ " /\===========║    | |___|_| |_|\_/ \___|_| |_|\__\__,_|_|  |_|\___/  ═══
|    ║         =| |\_/| |=#########║    |                                                  ══
|    ║         =\_>---<_/==========║    |  ═══════════════════════════════════════════════╝
|    ║          (___|___)          ║    |  ════          1 - COGUMELOS! (+5HP): {pocaoCura}          ══
|    ╚═════════════════════════════╝    |  ═══  2- Pedra de afiar dente (+2 Dano): {pocaoDano}       ══
 \_____________________________________/   ════           3 - Voltar                       ══
                                           ═══════════════════════════════════════════════╝
""")
    
    print("\n=============================================================================")
    print("\n      Selecione uma opção...")
    i = input()

    if i == "1" and pocaoCura >= 1:
        print("\nVOCÊ COMEU UM COGUMELO!")
        print("""
                .-"'"-.
               /* * * *\.
              :_.-:`:-._;
                  (_)
               \|/(_)\|/ """)
        personagemVida = personagemVida + 2
        pocaoCura = pocaoCura - 1
        print(f"\nSua vida agora é: {personagemVida} HP")
        input("Pressione para continuar...")

    elif i == "1" and pocaoCura == 0:
        print("Você não possui mais deste item!")
        input("Pressione para continuar...")
        ItemCapivara()

    elif i == "2" and pocaoDano >= 1:
        print("\nVocê afiou os dentes em uma pedra")
        print("""          
                    ______
                   /      \.
                  /        \#
                  \        /
                   \______/         """)
        
        input("\nPressione para continuar...")
        danoExtra = "1"
        pocaoDano = pocaoDano - 1

    elif i == "2" and pocaoDano == 0:
        print("Você não possui mais deste item!")
        input("Pressione para continuar...")
        ItemCapivara()

    elif i == "3":
        batalhaCapivara()

    else:
        ItemCapivara()

def usarItem():

    global pocaoCura
    global pocaoDano
    global personagemVida
    global danoExtra

    os.system('cls')
    print(f"""
  _____________________________________
 /                                     \  ════════════════════════════════════════════════╗
|    ╔═════════════════════════════╗    |  ___                      _    __       _        ══
|    ║                             ║    | |_ _|_ ____   _____ _ __ | |_ /_/_ _ __(_) ___   ═══
|    ║==========\///////\          ║    |  | || '_ \ \ / / _ \ '_ \| __/ _` | '__| |/ _ \. ════
|    ║          | _   _ |          ║    |  | || | | \ V /  __/ | | | || (_| | |  | | (_) | ════
|    ║=========( (o) (o) )=========║    | |___|_| |_|\_/ \___|_| |_|\__\__,_|_|  |_|\___/  ═══
|    ║          |  . .  |          ║    |                                                  ══
|    ║           \  _  /===========║    |  ═══════════════════════════════════════════════╝
|    ║            \___/            ║    |  ══          1 - KIT MÈDICO! (+5HP): {pocaoCura}           ══
|    ╚═════════════════════════════╝    |  ══  2- MUNIÇÃO EXPLOSIVA (+2 Dano): {pocaoDano}           ══
 \_____________________________________/   ══           3 - Voltar                         ══
   |______________________________O__|     ═══════════════════════════════════════════════╝

""")
    print("\n=============================================================================")
    print("Selecione uma opção...")
    i = input()

    if i == "1" and pocaoCura >= 1:
        print("\nVocê usou um kit médico!")
        print("""\n
            ______________
           /     __      /|
          /   __/ /_    / /
         /   /_  __/   / /
        /     /_/     / /
       /_____________/ / 
       |______8______|/
              """)
        personagemVida = personagemVida + 5
        pocaoCura = pocaoCura - 1
        print(f"\nSua vida agora é: {personagemVida} HP")
        input("Pressione para continuar...")

    elif i == "1" and pocaoCura == 0:
        print("Acabaram as drogas!")
        input("Pressione para continuar...")
        usarItem()

    elif i == "2" and pocaoDano >= 1:
        print("Você carregou a arma com munição traçante!")
        print("""
       _,________
      _T _==____()
     /##(_)-'  ______
    /##/      /BALAS/|
    '''      /__+__/ /
             |_____|/ 
""")
        print("\nSerá aplicado o dano no seu próximo turno")
        input("\nPressione para continuar...")
        danoExtra = "2"
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
            print(f"""
                
                ╔══════════════════════════════════════════════════╗
                ║                 ESCOLHA UMA AÇÃO                 ║
                ╠══════════════════════════════════════════════════╣
                    HUMANO: {personagemVida}                    CAPIVARA:{inimigoVida}        
                ╠════════════════╦════════════════╦════════════════╣  
                ║     ______     ║                ║        .       ║
                ║    /../../\    ║     ,===.      ║    __O/        ║
                ║    \-/**/-/    ║    )\ . /`     ║      /         ║
                ║     \__/_/     ║   /  `-´  \    ║  ;__/ \        ║
                ║      \__/      ║   \_ ___ _/    ║       |_       ║
                ╠════════════════╬════════════════╬════════════════║
                ║   1 - ATACAR   ║   2 - ITENS    ║   3 - FUGIR    ║
                ╚════════════════╩════════════════╩════════════════╝
                        """)
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
            os.system('cls')
            print("""
            ===============
            ATAQUE INIMIGO!
            ===============""")
            input()
            turnoInimigo()
            turno = "0"

        contarTurno = contarTurno + 1
    # JOGADOR DERROTA PRIMEIRO INIMIGO, SEGUNDO INIMIGO:
    if inimigoVida <= 0 and verificarMorto == "1":
        os.system('cls')

        print(f"""{RED}      
                     ╔════════════════════════════════════╗
                     ║[0]                              [0]║
                     ║ |                                | ║ 
                     ║ |{WHITE}             ___                {RED}| ║
                     ║ |{WHITE}          .="   "=._.---.       {RED}| ║
                     ║ |{WHITE}        ."         c ´ Y`p      {RED}| ║
                     ║ |{WHITE}       /   ,       `. \./       {RED}| ║
                     ║ |{WHITE}      |   '-.   /     /         {RED}| ║ 
                     ║ |{WHITE}     _|      )_-\ \_=.\         {RED}| ║
                     ║ |{WHITE}   .-'`------)))`=-'"`'"        {RED}| ║
                     ║ |                                | ║               
                     ║[0]                              [0]║               
                     ╚════════════════════════════════════╝{RESET}""")
        ler_texto3()
        input()
        os.system('cls')
        an.iniciar_animacao4()
        input()
        os.system('cls')
        print(f"""{DKG}
                                    {BLACK}/¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\.{DKG}
                                  {BLACK}=|{WHITE} R   E   C   O   M   P   E   N   S   A {BLACK}|={DKG}
                                    {BLACK}\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/{DKG}
              
                ╔═════════════════════════════════════════════════════════════════════════════════╗
                ║                                                                                 ║{BLACK}══╗{DKG}
                ║{WHITE}                       ______________       {DKG}                                     ║{BLACK}  ║{DKG} 
                ║{WHITE}                      /    {RED} __{WHITE}      /|      {DKG}                                     ║{BLACK}  ║{DKG} 
                ║{WHITE}                     /   {RED}__/ /_{WHITE}    / /      {DKG} _     ___                           ║{BLACK}  ║{DKG} 
                ║{WHITE}                    /   {RED}/_  __/{WHITE}   / /      {DKG}_| |_  (__ \.                         ║{BLACK}  ║{DKG}
                ║{WHITE}                   /     {RED}/_/{WHITE}     / /      {DKG}|_   _| / __/                          ║{BLACK}  ║{DKG}
                ║{WHITE}                  /_____________/ /         {DKG}|_|   \___)                          ║{BLACK}  ║{DKG}
                ║{WHITE}                 |______________|/{DKG}                                               ║{BLACK}  ║{DKG}
                ║                                 ____________                                    ║{BLACK}  ║{DKG}
                ║    ______________--------------|*{WHITE}KIT MÉDICO{DKG}*|--------------_________________    ║{BLACK}  ║{DKG}
                ╠═════════════════════════════════════════════════════════════════════════════════║{BLACK}  ║{DKG}
                ╠═════════════════════════════════════════════════════════════════════════════════║{BLACK}  ║{DKG}
                ║   _______________----------- __________________ ----------____________________  ║{BLACK}  ║{DKG}
                ║                             |*{WHITE}MUNIÇÃO ESPECIAL{DKG}*|                                ║{BLACK}  ║{DKG}
                ║{RED}    _,________                                {DKG}_     _                            ║{BLACK}  ║{DKG}
                ║{RED}   _T _==____()                             {DKG}_| |_  / |                           ║{BLACK}  ║{DKG}
                ║{RED}   /##(_)-'   ______                       {DKG}|_   _|  ||                           ║{BLACK}  ║{DKG}
                ║{RED}  /##/       /BALAS/|                        {DKG}|_|   |__|                          ║{BLACK}  ║{DKG}
                ║{RED}  ¯¯¯       /_____/ /{DKG}                                                            ║{BLACK}  ║{DKG}
                ║{RED}            |_____|/{DKG}                                                             ║{BLACK}  ║{DKG}
                ╚═════════════════════════════════════════════════════════════════════════════════╝{BLACK}  ║{DKG}
                   {BLACK} ╚════════════════════════════════════════════════════════════════════════════════╝{RESET}
""")
        input()
    
    
        pocaoCura = pocaoCura + 2
        pocaoDano = pocaoDano + 1

        input("...")
        os.system('cls')
        print(F"""{RED}     
                     ╔════════════════════════════════════╗
                     ║[0]{WHITE}           _,--""--,_         {RED}[0]║
                     ║ |{WHITE}       _,,-"          \.        {RED}| ║ 
                     ║ |{WHITE}   ,-o"                ;        {RED}| ║
                     ║ |{WHITE}  (*             \     |        {RED}| ║
                     ║ |{WHITE}   \w\     __,-"  )    |        {RED}| ║
                     ║ |{WHITE}    `,_   (((__,-"     L___     {RED}| ║
                     ║ |{WHITE}       ) ,---\  /\    / -- '    {RED}| ║ 
                     ║ |{WHITE}     _/ /     )_||   /          {RED}| ║
                     ║ |{WHITE}     ''''     '''|_ /           {RED}| ║
                     ║ |{WHITE}                 '''            {RED}| ║
                     ║[0]                              [0]║
                     ╚════════════════════════════════════╝{RESET}""")
        ler_texto4()

        input()

        os.system('cls')
        
        an.iniciar_animacao3()

        input()
        

        verificarMorto = "0"

    turno = "0"     # TURNO VIRA DO JOGADOR

    while personagemVida > 0 and inimigoVida <= 0 and inimigoVida2 > 0:      # BATALHA JOGADOR CONTRA SEGUNDO INIMIGO:
        os.system('cls')

        if turno == "0":
            print(f"""
                                            ╔══════════════════════════════════════════════════╗
                                            ║                 ESCOLHA UMA AÇÃO                 ║
                                            ╠══════════════════════════════════════════════════╣
                                                HUMANO: {personagemVida}                2ª CAPIVARA:{inimigoVida2}        
                                            ╠════════════════╦════════════════╦════════════════╣  
                                            ║     ______     ║                ║        .       ║
                                            ║    /../../\    ║     ,===.      ║    __O/        ║
                                            ║    \-/**/-/    ║    )\ . /`     ║      /         ║
                                            ║     \__/_/     ║   /  `-´  \    ║  ;__/ \        ║
                                            ║      \__/      ║   \_ ___ _/    ║       |_       ║
                                            ╠════════════════╬════════════════╬════════════════║
                                            ║   1 - ATACAR   ║   2 - ITENS    ║   3 - FUGIR    ║
                                            ╚════════════════╩════════════════╩════════════════╝
                        """)
            
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"Você escolheu: {jogadorEscolha}")

            if jogadorEscolha == "1":
                atacarSegundoInimigo()

            elif jogadorEscolha == "2":
                usarItem()
                atacarSegundoInimigo()

            elif jogadorEscolha == "3":
                fugir()

            else:
                print("Opção inválida...")
                atacarSegundoInimigo()

            turno = "1"

        if turno == "1" and inimigoVida2 > 0:
            os.system('cls')
            print("""
            ===============
            ATAQUE INIMIGO!
            ===============""")
            input()
            turnoSegundoInimigo()
            turno = "0"

        contarTurno = contarTurno + 1



    print(f"Total de turnos: {contarTurno}")
# BATALHA CAPIVARA CONTRA HUMANO =================================================================================
   
def atacarSegundohumano(): # ATACAR O SEGUNDO HUMANO

    global inimigoVida2
    global turno
    global danoExtra

    os.system('cls') # LIMPA TELA

    print(f"""
                    ╔══════════════════════════════════════════════════╗
    ╔═════════════  ║              ESCOLHA COMO ATACAR                 ║
    ║    |\_/|      ╠══════════════════════════════════════════════════╣
    ║   ( o"O )        CAPIVARA: {personagemVida}                 2º HUMANO:{inimigoVida2}        
    ║   /\ " /\     ╠════════════════╦════════════════╦════════════════╣  
    ║  | |\_/| |    ║                ║     _          ║   .-'V'"'V'-.  ║
    ║  \_>---<_/    ║     /./        ║    //===-      ║    \^     ^/   ║
    ║  (___|___)    ║    /./__       ║   ((==-        ║     \^   ^/    ║
    ╚══════════════ ║   (____)))     ║    .\===-      ║      \^_^/     ║
                    ║                ║                ║       ¯¯¯      ║
                    ╠════════════════╬════════════════╬════════════════║
                    ║   1 - COICE    ║   2 - GARRAS   ║  3 - MORDIDA   ║
                    ╚════════════════╩════════════════╩════════════════╝
                       
""")
    escolha = input("""\n       Escolha um ataque:
                """)

    if escolha == "1":
        print("\nATAQUE DE COICE!")
        dano = random.randint(0, 2)
        an.iniciar_animacaoE()
        
    elif escolha == "2":
        print("\nATAQUE DE GARRAS!")
        dano = random.randint(0, 4)
        an.iniciar_animacaoD()

    elif escolha == "3":
        print("ATAQUE DE MORDIDA!")
        dano = random.randint(0, 5)
        an.iniciar_animacaoC()
    else:
        print("\nVocê perdeu a chance de atacar!")
        dano = 0

    if dano > 0:
        print(f"\nVocê deu {dano} de dano!")
    
    if dano == 0:
        os.system('cls')
        print("\nVocê ERROU!")
        print("\n /\_/.")  
        print("( ´.` )  --> EU ESTAVA BRINCANDO")
        print(" \ w /")
        print("  \./")
    
    inimigoVida2 -= dano
    verificarDanoExtra()

    print(f"\nSua vida: {personagemVida}")
    print(f"Vida inimiga: {inimigoVida}")
    gameOverCheck()
    vencedor()
    input("Pressione Enter para continuar...")

    danoExtra = "0"


def batalhaCapivara():

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
            print(f"""
                                                   ___ 
                                                .="   "=._.---. 
                                             ."         c ` Y ´p
                                            /   ,       `.  W_/ 
                                           |   '-.   /     /  
                                        .._|      )_-\ \_=.\.
                                            \.'`----)))`=-'"`'"
                        ╔═══════════════════════════════════════════════════════╗
                        ║                          LIFE                         ║
                        ╠═══════════════════════════════════════════════════════╣
                            CAPIVARA: {personagemVida}                         HUMANO:{inimigoVida}        
                        ╠═══════════════════════════════════════════════════════╣
                        ║     1 - ATACAR     2 - USAR ITEM     3 - FUGIR        ║
                        ╚═══════════════════════════════════════════════════════╝
""")
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"A escolha do jogador foi {jogadorEscolha}")

            if jogadorEscolha == "1":
                ataque()

            elif jogadorEscolha == "2":
                ItemCapivara()    
                batalhaCapivara()

            elif jogadorEscolha == "3":
                fugir()

            else:
                print("Opção inválida...")
                batalhaCapivara()

            turno = "1"

        if turno == "1" and inimigoVida > 0:
            os.system('cls')
            print("""
            ===============
            ATAQUE INIMIGO!
            ===============""")
            input()
            turnoInimigo()
            turno = "0"

        contarTurno = contarTurno + 1
    # JOGADOR DERROTA PRIMEIRO INIMIGO, SEGUNDO INIMIGO:
    if inimigoVida <= 0 and verificarMorto == "1":
        os.system('cls')
        print("")
        print("Parabéns! Você derrotou um humano!")
        print(f"""{BLACK}
                                    /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\ /¯\.
                                  =|{WHITE} R   E   C   O   M   P   E   N   S   A {BLACK}|=
                                    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
              
                                ╔═══════════════════════════════════════════════╗
                                ║                                               ║{YELLOW}══╗{BLACK}
                                ║                                               ║{YELLOW}  ║{BLACK} 
                                ║                                               ║{YELLOW}  ║{BLACK} 
                                ║            .-"'"-.               _     ___    ║{YELLOW}  ║{BLACK}
                                ║           /* * * *\            _| |_  (__ \.  ║{YELLOW}  ║{BLACK}
                                ║          :_.-:`:-._;          |_   _| / __/   ║{YELLOW}  ║{BLACK}
                                ║              (_)                |_|   \___)   ║{YELLOW}  ║{BLACK}
                                ║           \|/(_)\|/                           ║{YELLOW}  ║{BLACK}
                                ║                                               ║{YELLOW}  ║{BLACK}
                                ║     _______-----|*COGUMELOS*|-----_______     ║{YELLOW}  ║{BLACK}
                                ╠═══════════════════════════════════════════════║{YELLOW}  ║{BLACK}
                                ╠═══════════════════════════════════════════════║{YELLOW}  ║{BLACK}
                                ║     _____----|*MUNIÇÃO ESPECIAL*|----____     ║{YELLOW}  ║{BLACK}
                                ║                                               ║{YELLOW}  ║{BLACK}
                                ║             ______               _     _      ║{YELLOW}  ║{BLACK}
                                ║            /      \            _| |_  / |     ║{YELLOW}  ║{BLACK}
                                ║           /        \          |_   _|  ||     ║{YELLOW}  ║{BLACK}
                                ║           \        /            |_|   |__|    ║{YELLOW}  ║{BLACK}
                                ║            \______/                           ║{YELLOW}  ║{BLACK}
                                ║                                               ║{YELLOW}  ║{BLACK}
                                ╚═══════════════════════════════════════════════╝{YELLOW}  ║{BLACK}
                                      {YELLOW}╚══════════════════════════════════════════════╝{RESET}
""")
        pocaoCura = pocaoCura + 2
        pocaoDano = pocaoDano + 1

        print("")
        input("...")
        print("")
        print("O humano consegue rastejar até o acampamento!")
        input("...")
        print("")
        print("Ele conta sobre o acontecido e seu amigo não acredita!!")
        input("""
                   """)
        print("")
        print("Ele pega uma arma maior e vem a sua caça!")
        input("""
                                       """""""    
                                       |""""""    
                         _________     O   C""    
                        //-------\\   /_     \    
L______________||O-----------------\   |____/_\ / 
-----------------||||| =========== /\ ____\    v|
                  OOOO-L______________          / 
                    --____||||___\<               
                          ||||    (|-- |          
                          ----
""")
        print("")

        verificarMorto = "0"

    turno = "0"     # TURNO VIRA DO JOGADOR

    while personagemVida > 0 and inimigoVida <= 0 and inimigoVida2 > 0:      # BATALHA JOGADOR CONTRA SEGUNDO INIMIGO:
        os.system('cls')

        if turno == "0":
            print(f"""
                                                   ___ 
                                                .="   "=._.---. 
                                             ."         c ` Y ´p
                                            /   ,       `.  W_/ 
                                           |   '-.   /     /  
                                        .._|      )_-\ \_=.\.
                                            \.'`----)))`=-'"`'"
                        ╔═══════════════════════════════════════════════════════╗
                        ║                          LIFE                         ║
                        ╠═══════════════════════════════════════════════════════╣
                            CAPIVARA: {personagemVida}                      2º HUMANO:{inimigoVida2}        
                        ╠═══════════════════════════════════════════════════════╣
                        ║     1 - ATACAR     2 - USAR ITEM     3 - FUGIR        ║
                        ╚═══════════════════════════════════════════════════════╝
""")
            
            jogadorEscolha = "0"
            jogadorEscolha = opcaoBatalha()
            print(f"Você escolheu: {jogadorEscolha}")

            if jogadorEscolha == "1":
                atacarSegundohumano()

            elif jogadorEscolha == "2":
                ItemCapivara()
                batalhaCapivara()

            elif jogadorEscolha == "3":
                fugir()

            else:
                print("Opção inválida...")
                batalhaCapivara()

            turno = "1"

        if turno == "1" and inimigoVida2 > 0:
            os.system('cls')
            print("\n==============")
            print("ATAQUE HUMANO!")
            print("==============")
            input()
            turnoSegundoInimigo()
            turno = "0"

        contarTurno = contarTurno + 1
        vencedor()


    print(f"Total de turnos: {contarTurno}")
# COMEÇAR O JOGO: =================================================================================
def startJogo():
    global personagemVida
    global inimigoVida
    global inimigoVida2

    os.system('cls') # LIMPA TELA

    selecionarClasse()

    if personagemClasse == "1":
        batalhaHumano()

    elif personagemClasse == "2":
        batalhaCapivara()

    else:
        print("Opção inválida...")
        selecionarClasse()

#ZEROU O JOGO ===========================
def vencedor():
    if personagemClasse == "2" and inimigoVida2 <= 0:
        os.system('cls')
        print("""
     
        ('(               _____                _ 
          \ \            |  __ \              | |       // 
       d@b | |           | |__) |_ _ _ __ __ _| |__   ___ _ __  ___
       @@@@' |           |  ___/ _` | '__/ _` | '_ \ / _ \ '_ \/ __|
   ('(  Y@P   `--..      | |  | (_| | | | (_| | |_) |  __/ | | \__ *
    \ `--'      .' `.    |_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___/
     `---....__/    |                 
        |      /   . \                                 
        |     /  .'\  \      /\_/.  --->VOCÊ DERROTOU OS HUMANOS!!!!!
        |     \  \  \  \    ( `.< ) 
    -SOCORRO-  \  \  \__\    \ w / `~+++,,_______
               _`--` `--'     \./ ............../
              `---'              \ ............./    
                                    HH        HH
                                    WW        WW
         
          """)
        input()
        quit()
    if personagemClasse == "1" and inimigoVida2 <= 0:
        os.system('cls')
        an.iniciar_animacao4()
        input("Enter para sair")
        quit()

# MAIN():       
menu()