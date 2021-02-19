salario = float(input('Informe o salário: '))
if salario > 1250:
    aumento = (salario * 10)/100
else:
    aumento = (salario * 15)/100
print(f'O seu salário é R${salario} então teve um aumento de R${aumento} \nValor final R${salario + aumento}')