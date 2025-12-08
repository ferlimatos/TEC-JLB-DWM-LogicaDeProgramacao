# Exercício 1
# Criação e Inserção Simples
# Crie uma lista vazia chamada marcas_carros. Use o método .append() para adicionar três marcas de carro de sua preferência. Ao final, imprima a lista completa.

marcas_carros = []

for i in range(3):
  marca = input("Digite uma marca de carro: ")
  marcas_carros.append(marca)

print("Lista final:", marcas_carros)