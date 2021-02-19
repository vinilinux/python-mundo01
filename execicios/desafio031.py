km = int(input('Qual a distância da viagem(km): '))
'''if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45'''
valor = km * 0.50 if km <= 200 else km * 0.45
print(f'O valor da viagem é R${valor:.2f}')