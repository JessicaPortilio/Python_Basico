"""
For / Else
"""

variavel =['Luiz', 'João', 'Maria']
comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'): #verificar se começa com tal letra
        print('Existe uma palavra que começa com J')
        break
else:
    print('Não existe uma palavra que começa com J.')