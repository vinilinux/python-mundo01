frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A frase possui {frase.count("a")} letra(s) A')
print(f'A letra A aparece pela primeira vez na posição {frase.find("a")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("a")+1}')
