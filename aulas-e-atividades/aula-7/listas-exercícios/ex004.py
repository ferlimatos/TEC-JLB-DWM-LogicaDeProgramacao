# Exercício 4
# Peça ao usuário uma fruta para adicionar e uma posição para inserir. Use insert() para colocar a fruta na posição indicada.

frutas = ["uva", "banana", "maçã", "pera"]
print(f"Lista original de frutas: {frutas}")

nova_fruta = input("Digite o nome da fruta que deseja adicionar: ")

posicao_inserir = int(input("Em qual índice (posição) deseja inserir a fruta? (Ex: 0 para o início): "))
frutas.insert(posicao_inserir, nova_fruta)

print("\nFruta inserida com sucesso!")
print(f"Lista após inserção: {frutas}")
