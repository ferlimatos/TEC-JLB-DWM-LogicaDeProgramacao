soma = 0
quantidade = 0

idade = int(input('Informe uma idade: '))

while idade != 0:
  soma = soma + idade
  quantidade = quantidade + 1
  idade = int(input("Digite uma nova idade: "))

if quantidade > 0:
  media = soma / quantidade
  print(f'Total de idades válidas: {quantidade}')
  print(f"Média das idades: {media:.2f} anos.")
else:
  print("Nenhuma idade foi digitada para o cálculo da média.")
