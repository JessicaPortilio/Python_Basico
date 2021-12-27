nome = 'Jessica'
idade = 29
altura = 1.60
e_maior = idade > 18
peso = 58
imc = peso / altura ** 2
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} ten {idade} anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i} anos de idade e seu imc é {im} '.format(n=nome, i=idade, im=imc))