import sys
from time import sleep
from random import randint
from colorama import *




#=========================== CavaleirosVendetta ===============================#
classes = ['Barbaro', 'Mago', 'Ninja']
id_jogador = randint(0, 2) # Escolhe aleatoriamente classe do jogador.
vida_jogador, vida_monstro = randint(20, 30), randint(25, 35) 
ataques_monstro = ['garras', 'presas', 'magias de goblin']
acao_monstro = ['se esquiva', 'se defende', 'grita']
turno, m_dano, ataque = 1, 0, 0
forca, magia = 0, 0

def limpar_tela(): #Realiza a limpeza do sistema utilizando CLS
    init(wrap=False)
    AnsiToWin32(sys.stderr).write("\x1b[2J\x1b[H")

def informa(): #Informação dano no inimigo
    print(Back.RED +F'Você recebe {dano_monstro} de dano e fica com {vida_jogador} de vida.' + Style.RESET_ALL + '\n' +'-'*80)

def atacou(): #Executa ataque
    global vida_monstro
    vida_monstro -= randint(2, 5) 
    print(Back.RED + "="*vida_monstro + Style.RESET_ALL +  F' {vida_monstro}HP\n' + '-'*80)
    sleep(3)

#Definições das classes.
if id_jogador == 0: #Barbaro   
    forca = 25
    magia = 10
elif classes == 1: # Mago
    forca = 10
    magia = 25
else: #Ninja
    forca = 15
    magia = 15

# TELA DE INTRODUÇÃO AO JOGO
limpar_tela()
print('''
| ============================================================================ |
|                                 CAVALEIROS VENDETTA                          |
| ============================================================================ |
''')
print(F'''Você será um {classes[id_jogador]}! seus atributos são: {vida_jogador} de vida, {forca} de forca e {magia} de magia\n''' + '-'*80)
sleep(8)

#Começo do jogo
while vida_monstro > 1:
    print(Back.BLUE +  ' '*29 + F'TURNO {turno}' + ' '*25 + Style.RESET_ALL)
    print(' '*15 + Back.LIGHTBLACK_EX + F'Você tem {vida_jogador}HP o monstro tem {vida_monstro}HP' + Style.RESET_ALL + '\n' + '-'*80 )
    print(' '*22 + 'ESCOLHA SEU ATAQUE')
    print('1 - NENHUM | 2 - ESPADADA [-5 F] | 3 - MAGICO [-2 M|')
    ataque = int(input(F'Qual ataque deseja usar: '))
    print('-'*63)
    sleep(2)
    if ataque == 1: #Nenhum / Pular Round
        print('Você decidiu pular o seu round, é a vez do inimigo!\n' + '-'*80)
        print(Back.LIGHTGREEN_EX + F'O Monstro ataca com suas {ataques_monstro[randint(0, 2)]}!!!' + Style.RESET_ALL)
        dano_monstro = randint(2,7)
        vida_jogador = vida_jogador - dano_monstro
        informa() # Sempre que for recomeçar o round, exibe os status atuais.
    elif ataque == 2: #Espada
        print(F'Você desfere um golpe de espada no monstro!')
        atacou() #Como será o ataque
    elif ataque == 3: #Magico
        vida_monstro = 1
    turno += 1
    sleep(5)
limpar_tela()
print(' '*24 + Back.LIGHTGREEN_EX + 'FIM DO JOGO!' + Style.RESET_ALL + '\n' + '-'*80)
print('REVISÃO DA SUA JORNADA!')
print(F'O jogo terminou no turno: {turno}.')
print(F'Você ficou com: {vida_jogador} de vida.')
print(F'O monstro ficou com: {vida_monstro} de vida.')
if vida_monstro <= 0:
    print(' '*24 + Back.LIGHTYELLOW_EX + 'Você Venceu!' + Style.RESET_ALL + '\n' + '-'*80)
elif vida_jogador <= 0:
    print(' '*24 + Back.LIGHTRED_EX + 'Você Perdeu!' + Style.RESET_ALL + '\n' + '-'*80)
