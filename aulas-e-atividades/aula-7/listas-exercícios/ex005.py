# Exercício 5
# Crie uma lista com alguns números misturados. Use sort() para ordenar: em ordem crescente e em ordem decrescente.

numeros = [5,7,1,15,31]
print(f'Lista original: {numeros}')

numeros.sort()
print("Ordem Crescente (usando .sort()):")
print(numeros)

numeros_decrescente = sorted(numeros, reverse=True)
print("\nOrdem Decrescente (usando sorted(reverse=True)):")
print(numeros_decrescente)



