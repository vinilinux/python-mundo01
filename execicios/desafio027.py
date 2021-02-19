nome = input('Digite seu nome: ').strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')

'''Poderíamos usar apenas  nome[-1]  que teríamos o mesmo resultado, no caso sempre a ultima palavra da frase, exemplo:
print('Seu último nome é {}'.format(nome[-1] )) 


No caso o número positivo começaria da esquerda para a direita e os números negativos da direta para esquerda.'''