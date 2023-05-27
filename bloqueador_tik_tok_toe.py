from random import randint
from time import sleep

def separador():
    print('=' * 30)
 
def apresentaJogo():
    print('VAMOS JOGAR O JOGO DA VELHA')
    separador()
    sleep(1)
    print('Você vai precisar informar um número entre 1 e 9.')
    sleep(0.5)
    print('Fique atento!!!')
    sleep(1)

def jogada():
    n1 = int(input('Informe a posição em que você deseja iniciar o jogo, representando de 1 a 9: '))
    n2 = randint(1, 9)
    return n1, n2

def bloquearJogada():
    vencedora = [
        [1,2,3],[4,5,6],[7,8,9],
        [1,4,7],[2,5,8],[3,6,9]
        [1,5,9],[3,5,7]
    ]


separador()
apresentaJogo()
separador()
n1, n2 = jogada()
print('Você escolheu a posição representada pelo número', + n1)
print('...o computador escolheu a posição representada pelo número ', n2)
print('FIM!!!')
