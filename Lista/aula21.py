"""
Lista
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# #         0    1         2    3    4
# lista = ['A', 'Banana', 'C', 'D', 'E']
# #       - 5    4         3    2    1
#
# lista[3] = 10.2
#
# print(lista)
#
# print(lista[0:3])
# print(lista[::2])
# print(lista[::-1])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.extend(l2)
# print(l2)
# l2.append('b')
# print(l2)
# l2.pop()
# print(l2)
#
# print(l1)
# print(l2)

# l2 = [1,2,3,4,5,6,7,8,9]
# print(max(l2))
# print(min(l2))
# del(l2[3:5])
# print(l2)

# l2 = list(range(0, 100, 8))
# print(l2)
# print(l2[3])

# l2 = ['String', True, 10, -20.4]
# for elem in l2:
#     print(f'O tipo de elem é {type(elem)} e seu valor [e {elem}')

secreto = input('Iforme a palavra secreta? ').lower()
digitadas = []
chances = 10
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite somente uma letra!')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'UHULLLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFzzzz a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
            print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()