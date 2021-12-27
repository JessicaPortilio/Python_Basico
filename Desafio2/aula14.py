import re

#verificar se o que usuário digitou pode ser convertido para float
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

#verificar se o que usuário digitou pode ser convertido para int
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

#verificar se o que usuário digitou pode ser convertido para numero
def is_number(val):
    return is_int(val) or is_float(val)
"""
Faça um programa que peça ao usuário para digitar um número inteiro. informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, nforme que não é um número
"""
num = input("Informe um número: ")
if is_number(num):
    num = int(num)
    if (num % 2) == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')
else:
    print('Você não digitou um número')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudaão apropriada.
Ex.
Bom dia 0 - 11, Boa tarde 12 - 17 e Boa noite 18 -23
"""
hora = input("Informe a hora: ")
if is_number(hora):
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Você não digitou um horario invalido (0 á 23)')
    else:
        if hora == 0 or hora <= 11:
            print('Bom dia!')
        elif hora == 12 or hora <= 17:
            print('Boa Tarde!')
        else:
            print('Boa noite!')
else:
    print('Você não digitou um horario invalido (0 á 23')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""
nome = input("Qual seu nome? ")
qtd_caracteres = len(nome)

if qtd_caracteres <=4:
    print("Seu nome é curto!")
elif qtd_caracteres > 4 and qtd_caracteres <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")