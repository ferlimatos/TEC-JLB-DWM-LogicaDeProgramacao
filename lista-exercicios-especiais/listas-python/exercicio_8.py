# Exercício 8
# Média Aritmética e Soma Total
# Crie uma lista de 6 números inteiros. 
# a. Use a função sum() para calcular a soma de todos os elementos. 
# b. Use a função len() para obter o número total de elementos. 
# c. Calcule a média dos números (soma / quantidade de elementos) e imprima a soma total e a média.

num_inteiros = [10,57,81,120,150,197]
print(f"Lista de números inteiros: {num_inteiros}")

print(f"O resultado da soma dos números inteiros da lista é: {sum(num_inteiros)}")

print(f"O total de elementos da lista é: {len(num_inteiros)}")

media_num_inteiros = (sum(num_inteiros) / len(num_inteiros))
print(f"A média dos números inteiro da lista é {media_num_inteiros} e a soma total é {sum(num_inteiros)}.")