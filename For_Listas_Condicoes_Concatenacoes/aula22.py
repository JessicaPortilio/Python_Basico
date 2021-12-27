# secreto_temporario = ''
# for letra_secreta in secreto:
#     if letra_secreta in digitadas:
#         secreto_temporario += letra_secreta
#     else:
#         secreto_temporario += '*'


secreto = 'perfume'
secreto_temporario = ''

digitadas = ['e']

for letra_secreta in secreto:
    print(f'Iteração para a letra {letra_secreta}')

    if letra_secreta in digitadas:
        print(f'Eba, a letra que eu queria {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        secreto_temporario += '*'
print(secreto_temporario)