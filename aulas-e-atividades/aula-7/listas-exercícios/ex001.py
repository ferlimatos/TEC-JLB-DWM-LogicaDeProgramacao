# Exercício 1
# Crie uma lista vazia chamada numeros. Peça ao usuário para digitar 5 números e use append() para guardar todos na lista. Ao final, imprima a lista completa.

numeros = []  # Lista vazia

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("\nSua lista de números completa:")
print(numeros)
