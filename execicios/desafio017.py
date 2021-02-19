'''from math import hypot
ca = float(input('Cateto Adjacente: '))
co = float(input('Cateto Oposto: '))
print(f'O valor da Hipotenusa é {hypot(ca, co):.2}')'''

# Outra maneira de fazer

ca = float(input('Cateto Adjacente: '))
co = float(input('Cateto Oposto: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da Hipotenusa é {hi:.2}')