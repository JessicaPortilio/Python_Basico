"""
Variaves devem iniciar com letra, pode conter números, separar _, letras minúscilas
"""
nome = 'Jessica'
idade = 29
altura = 1.60
e_maior = idade > 18
peso = 58
print('Nome:', nome, type(nome))
print('Idade:', idade, type(idade))
print('Altura:', altura, type(altura))
print('É maior de idade:', e_maior, type(e_maior))
imc = peso / altura ** 2
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
