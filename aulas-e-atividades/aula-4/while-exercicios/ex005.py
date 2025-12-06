# Exercício 5

# Leia as idades de um grupo até o usuário digitar 0. Calcule a média das idades.

soma = 0   
quantidade = 0

idade = int(input("Digite uma idade (0 para encerrar): "))
while idade != 0:
  soma += idade
  quantidade += 1
  idade = int(input("Digite uma idade (0 para encerrar): "))

if quantidade > 0:
  media = soma / quantidade
  print(f"A média das idades é: {media}.")
else:
    print("Nenhuma idade foi informada.")