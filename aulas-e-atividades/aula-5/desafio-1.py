# Desafio 1

# Peça para que o usuário digite o start, stop, step do seu range 
# e imprima o resultado em uma mesma linha.

start = int(input('Digite um número para ser start: '))
stop = int(input('Digite um número para ser stop: '))
step = int(input('Digite um número para step: '))

print('Números no intervalo escolhido: ')
for numeros in range(start, stop, step):
    print(numeros, end = ', ')

# Explicação: Neste exemplo, o parâmetro `end=", "` é 
# usado na instrução `print()` para imprimir cada número no intervalo 
# na mesma linha, separados por vírgula e espaço. Sem ele, 
# cada número seria impresso em uma nova linha por padrão.