"""
For in
Iterando strings com for
Função range(start = 0, stop, step=1)
"""
texto = 'Python'
#
# for letra in texto:
#     print(letra)
#

# for numero in range(10):
#     print(numero)

nova_strign = ''
for letra in texto:
    if letra == 't':
        nova_strign += letra.upper()
    else:
        nova_strign += letra
print(nova_strign)