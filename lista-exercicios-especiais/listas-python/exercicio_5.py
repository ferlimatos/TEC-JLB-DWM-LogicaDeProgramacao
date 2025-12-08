# Exercício 5
# Remoção por Valor
# Crie a lista de frutas: ['maçã', 'banana', 'laranja', 'morango', 'banana']. 
# a. Peça ao usuário para digitar uma fruta que deseja remover (ex: 'banana'). 
# b. Use o método .remove() para retirar a fruta da lista (lembre-se que ele remove apenas a primeira ocorrência). 
# c. Imprima a lista final.

frutas = ['maçã', 'banana', 'laranja', 'morango', 'banana']
print(f"Lista inicial: {frutas}")

remover_fruta = input("Digite uma fruta que deseja remover da lista (maçã, banana, laranja, morango, banana): ").lower()

frutas.remove(remover_fruta)
print(f"Lista após .remove(): {frutas}")


