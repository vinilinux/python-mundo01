dias = int(input('Quantos dias alugados? '))
km = int(input('Qunatos KM percorridos? '))

valor = (dias * 60) + (km * 0.15)

print(f'O valor a ser pago é de R${valor}')
