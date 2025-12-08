# Exercício 4
# Ordenação Alfabética e Inversão
# Crie uma lista chamada cores com 4 nomes de cores diferentes. 
# a. Use o método .sort() para ordenar a lista em ordem alfabética e imprima o resultado. 
# b. Use o parâmetro reverse=True com .sort() para ordenar a lista em ordem alfabética decrescente e imprima o resultado.

cores = ['preto', 'rosa', 'roxo', 'amarelo']
print(f"Lista inicial: {cores}")
print("---" * 30)

cores.sort()
print(f"Lista após .sort() em ordem alfabética: {cores}")
print("---" * 30)

cores.sort(reverse=True)
print(f"Lista após .sort(reverse=True): {cores}")
