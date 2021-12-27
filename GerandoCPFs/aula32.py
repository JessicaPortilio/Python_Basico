from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero                # Elimina os dois últimos digitos do CPF
reverso = 10                        # Contador reverso
total = 0

# Loop do CPF
for index in range(19):             # Precisamos da 19 volta
    if index > 8:                   # Primeiro índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF
    # print(novo_cpf[index], reverso)
    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação
    # print(total)
    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        # print(total)
        d = 11 - (total % 11)
        # print(d)
        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf
        # print(novo_cpf)
print(novo_cpf)