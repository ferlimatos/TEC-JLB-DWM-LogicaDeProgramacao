# Tem que usar while para fazer a soma dos números

soma = 0
contador = 1

while contador <= 5:
    numero = int(input(f'Digite o {contador}º número: '))
    soma += numero
    contador += 1
    
print(f'A soma dos números é: {soma}')