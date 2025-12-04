numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
operacao = str(input("Escolha uma operação (+,-,*,/): "))

resultado = None 

if operacao == "+":
  resultado = numero_1 + numero_2
elif operacao == "-":
    resultado = numero_1 - numero_2
elif operacao == "*":
    resultado = numero_1 * numero_2
elif operacao == "/":
  if numero_2 != 0:
      resultado = numero_1 / numero_2
  else:
    print("Não é possível dividir por zero.")
else:
   print("Operação inválida.")

if resultado is not None:
  print(f"A operação gerada é {numero_1} {operacao} {numero_2}.")
  print(f"O resultado da operação é {resultado}.")




