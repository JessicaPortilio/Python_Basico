#        Indices
#        0123456789......................33
frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)

contador = 0
nova_string = ''
escolha_do_usuario = input("Qual letra deseja colocar maiuscula? ")

# Iteração <- Interar
while contador < tamanho_frase:

    letra = frase[contador]
    if letra == escolha_do_usuario:
        nova_string += escolha_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
