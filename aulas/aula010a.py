'''nome = str(input('Qual é seu nome? ')).title()
if nome == 'Vinicius':
    print('Que nome lindo')
else:
    print('Seu nome é tão normal')
print(f'Bom dia {nome}')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim')