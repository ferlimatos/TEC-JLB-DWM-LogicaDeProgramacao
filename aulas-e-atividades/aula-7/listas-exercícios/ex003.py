# Exercício 3
# Crie uma lista com 6 nomes, peça ao usuário um número de posição (índice) e remova o nome daquela posição usando del ou pop.

nomes = ["Isabela", "Gabriela", "Fernanda", "André", "Mariana", "Ana"]
print(f'Lista original: {nomes}')

posicao_indice = int(input("Informe o índice (0 a 5) que deseja remover da lista: "))

nome_removido = nomes.pop(posicao_indice)

print(f"\nRemovido o nome '{nome_removido}' do índice {posicao_indice}.")
print(f"Lista após remoção: {nomes}")