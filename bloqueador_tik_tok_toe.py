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

def bloquearJogada(n1, n2):
    vencedora = [
        [1,2,3],[4,5,6],[7,8,9],
        [1,4,7],[2,5,8],[3,6,9],
        [1,5,9],[3,5,7]
    ]
    for jogada in vencedora:
        if(n1 in vencedora) and (n2 in vencedora):
            listaVazia = []
            for elemento in vencedora:
                if elemento != n1 and elemento != n2:
                    listaVazia.append(elemento)
                    break
            if listaVazia is not None:
                return listaVazia
    return None

separador()
apresentaJogo()
separador()
n1, n2 = jogada()
pontoDeBloqueio = bloquearJogada(n1,n2)

if pontoDeBloqueio is not None:
    print('Número do ponto que impede a vitória ', + pontoDeBloqueio,'.')
else:
    print('Não há ponto que impela a vitório dos jogadores.')

print('FIM!!!')
