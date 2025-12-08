# Exercício 9
# Gestão de Estoque (Insert e Del)
# Simule uma pequena gestão de estoque com a lista: estoque = ['caderno', 'caneta', 'lápis', 'régua']. 
# a. O usuário informa um novo item (ex: "borracha") e o índice onde ele deve ser inserido (ex: 1). Use .insert(). 
# b. O programa pergunta qual índice de item deve ser removido por estar esgotado (ex: 3). Use del. 
# c. Imprima o estado final do estoque.

estoque = ['caderno', 'caneta', 'lápis', 'régua']
print(f"Lista de estoque inicial: \n{estoque}")

novo_item = input("Informe um item que você deseja adicionar na lista de estoque: ").lower()
indice_item = int(input("Informe a posição de um índice: "))
estoque.insert(indice_item,novo_item)
print(f"Lista de estoque após .insert(): \n{estoque}")

print("Atenção! A lista do estoque está ESGOTADA.")
item_removido = int(input("Um item precisa ser removido. Informe seu índice para que seja removida da lista: "))
del estoque[item_removido]
print(f"Lista do estoque após remoção do item: \n{estoque}")


