# Exercício 2
# Usando a lista do exercício anterior, imprima:
# a. o maior número (max)
# b. o menor número (min)
# c. a soma dos números (sum)
# d. a média dos números

numeros = [5, 10, 20, 50, 100]

maior_numero = max(numeros)
print(f"a. O maior número da lista é: {maior_numero}")

menor_numero = min(numeros)
print(f"b. O menor número da lista é: {menor_numero}")

soma_dos_numeros = sum(numeros)
print(f"c. A soma dos números da lista é: {soma_dos_numeros}")

quantidade = len(numeros)
media = soma_dos_numeros / quantidade

print(f"d. A média dos números da lista é: {media:.2f}")
