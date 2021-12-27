"""
Desempacotamento de listas
"""
lista = ['Luiz', 'João', 'Maria',1,2,3,4,5,6,7,8,9]

n1, n2, n3, *outra_lista = lista

print(n1, n2, n3, outra_lista)