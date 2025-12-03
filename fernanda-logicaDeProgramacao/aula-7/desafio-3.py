# Desafio 3

# Peça para o usuario digitar itens de uma lista e compras e 0 para parar, quando parar, imprima a lista de compras com o título “Lista de compras”

lista_compras = []
item = input("Adicione um item para a inserir em sua lista de compras (ou 0 para parar): ")

while item != "0":
  lista_compras.append(item)
  item = input("Adicione um item para a inserir em sua lista de compras (ou 0 para parar): ")

print("\nSua lista de compras:")
print(lista_compras)