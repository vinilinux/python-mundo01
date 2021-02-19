n = float(input('Digite a velocidade do carro(KM): '))
if n > 80:
    multa = (n - 80) * 7
    print(f'Você foi multado \nvalor da multa R${multa:.2f}')
else:
    print(f'Sua velocidade foi de {n}KM/H, tenha um bom dia!')

