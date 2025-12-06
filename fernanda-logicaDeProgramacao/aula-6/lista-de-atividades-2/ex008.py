# Exercício 8

# Crie um algoritmo que peça para o usuário digitar um número qualquer e imprima na tela se esse número é par ou ímpar, e positivo ou negativo.

'''==================================='''

'''Minha resposta:'''

numero = int(input("Digite um número qualquer: "))

if numero % 2 == 0:
    tipo = "par"
else:
    tipo = "ímpar"

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "nem positivo nem negativo"

print(f"O número {numero} é {tipo} e {sinal}.")
