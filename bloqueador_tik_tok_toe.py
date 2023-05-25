from random import randint

print('====VAMOS JOGAR O JOGO DA VELHA===')
print('Você vai precisar informar dois números entre 1 e 9.')

n1 = input('Informe o primeiro número: ')
print(n1)

n2 = randint(1,9)
print('O número escolhido pelo computador foi: ',+ n2)
print(n2)

print('FIM!!!')
