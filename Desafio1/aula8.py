"""
* Criar variáveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Jessica'
idade = 29
altura = 1.60
peso = 58
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura **2
print(f'Nome:  {nome} tem {idade} anos e tem {altura} de altura e pesa {peso}kg. Nasceu {ano_nascimento} e seu imc é {imc:.2f}')