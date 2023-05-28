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
        if n1 in jogada and n2 in jogada:
            listaVazia = []
            for elemento in jogada:
                if elemento != n1 and elemento != n2:
                    listaVazia.append(elemento)
                    break
            if listaVazia:
                return listaVazia[0]
    return None

separador()
apresentaJogo()
separador()
sleep(1.5)
print('...Carregando Informações...')
sleep(2.5)

n1, n2 = jogada()
print('Aguarde o computador jogar...')
sleep(2)
print('PROCESSANDO JOGADAS, mais um momento por favor...')
sleep(3)
pontoDeBloqueio = bloquearJogada(n1,n2)

if pontoDeBloqueio is not None:
    print('O número do ponto que pode impedir que esses dois pontos ganhem o jogo, '
        'foi representado pelo número', pontoDeBloqueio,'.')
else:
   print('Não há ponto que impeça a vitória dos jogadores.')

print('FIM!!!')
