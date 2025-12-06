# Desafio 1

# Crie uma lista com pelo menos 5 frutas, ordene a lista em ordem alfabética e imprima o primeiro elemento dessa lista.
# Depois, substitua alguma fruta por “tamarindo” e imprima novamente.

frutas = ["banana", "maçã", "maracujá", "mamão", "laranja"]
frutas.sort()
print(frutas)

frutas[0] = "tamarindo"
print(frutas)