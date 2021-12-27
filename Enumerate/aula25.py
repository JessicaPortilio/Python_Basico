"""
* Enumerate - Enumerar elementos da lista #list /Iteráveis
"""

lista = [
    # 0       1       2
    ['Edu', 'João', 'Luiz'], # 0
    ['Maria', 'Aline', 'Patricia'], # 1
    ['Vanessa', 'Téu', 'Pedro'] # 2
]

# print(lista[2][1])
#
# enumerada = list(enumerate(lista))
# print(enumerada[0][0])
# print(enumerada[0][1])
# print(enumerada[1][0])
# print(enumerada[1][1])
# print(enumerada[2][0])
# print(enumerada[2][1])
# print(enumerada[1][1][1])
# print(enumerada[2][1][2])

"""
[ < -- Enumerate

     0  1
    (0, ['Edu', 'João', 'Luiz']), 
    (1, ['Maria', 'Aline', 'Patricia']), 
    (2, ['Vanessa', 'Téu', 'Pedro'])
]
"""

for valor in enumerate(lista, 1):
    valor_enumerado, minha_lista = valor

    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2)