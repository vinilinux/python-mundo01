print('\033[mOlá, Mundo!\033[m')

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')

nome = 'Vinicius'
core = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, {core["pretoebranco"]}{nome}{core["limpa"]}')
