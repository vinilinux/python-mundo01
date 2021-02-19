'''from random import choice
n = int(input('Digite um número: '))
print('pensando...')
p = choice([0, 1, 2, 3, 4, 5])
if n == p:
    print(f'PARABÉNS, você acertou')
else:
    print(f'ERROU, o número era {p}! \nTENTE DE NOVO')'''


from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você venceu!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')

