"""
Split, Join e Enumerate
* Split - Dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #list /Iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."
print('****************Split***********************')
lista = string.split(' ')
print(lista)
string2 = ' '.join(lista)
lista2 = string.split(',')
print(lista2)
palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})')
print('***************************************')
print('****************Join***********************')
print(string)
print(lista)
print(string2)
print('***************************************')
print('******************strip / Capitalize*********************')
for valor2 in lista2:
    print(valor2.strip().capitalize()) #retira o espaço vazio do começo e deixar a primeira letra em mauscula

print('***************************************')

print('***************Enumerate************************')
string = 'O Brasil é penta'
lista6 = string.split(' ')

for indice, valor in enumerate(lista6):
    print(indice, valor, lista[indice])
print('***************************************')