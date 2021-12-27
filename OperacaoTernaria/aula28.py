"""
Operador ternário
"""

logged_user = False

# if logged_user: #se for verdadeiro
#     msg = 'Usuario logado'
# else:
#     msg = 'Usuario precisa logar'
# print(msg)


# msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar'
#
# print(msg)

idade = input('Qual sua idade? ')

# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')
if not idade.isnumeric():
    print('Isso não é uma idade valida!')
else:
    idade = int(idade)
    eh_maior = (idade >=18)
    msg = 'Pode acessar' if eh_maior else 'Não pode acessar'

    print(msg)