# Exercício 6
# Lista de Compras Dinâmica (Input e Append)
# Crie um programa que permita ao usuário criar uma lista de compras. 
# a. Crie uma lista vazia (compras = []). 
# b. Use um laço for para pedir ao usuário que digite 5 itens para adicionar à lista. 
# c. A cada item digitado, use .append() para adicioná-lo. 
# d. Imprima a lista de compras completa.

lista_de_compras = []

for i in range(5):
  item = input("Informe um item para ser adicionado na lista de compras: ")
  lista_de_compras.append(item)

print(f"Lista de compra gerada:\n{lista_de_compras}")

