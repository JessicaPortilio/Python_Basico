"""
Manipulando strings
* String indices
* Fatiamento de strings [Inicio:fim:passo]
* Funções buit-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
#positivos    [012345678]
texto =       'Python s2'
#negativos   -[987654321]
texto_2 = 'Python s2'
print(texto[5])

nova_string = texto[2:6]    # vai começar do indice 2 't' e vai até o indice 6
print(nova_string)

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto_2[0::3]     # vai começar do começo indo até o final pulando de 3 em 3

x = 1
y = 5
print(texto[x:y])