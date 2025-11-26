# while é um comando usado em programação para repetir uma ação enquanto uma condição for verdadeira.
# qual é a estrutura básica do while em Python?

'''
# while = repetir algo
# Só para quando a condição fica falsa
# Cuidado para evitar loop infinito (quando nunca para!)
'''

# Exemplo 1: Imprimir números de 1 a 9

n = 1
while n < 10:
    print(n)
    n += 1

# Exemplo 2: Senha de acesso

senha_correta = 'python123'
tentativa = input('Digite a senha: ')

while tentativa != senha_correta:
    print('Senha incorreta! Tente novamente.')
    tentativa = input('Digite a senha: ')

print('Acesso liberado!')

'''
# Condição de Parada 

'''

n = 1

while n < 10:
    print(n)
    if n == 5:
        break  # Interrompe o loop quando n é igual a 5
    n += 1

print('Loop encerrado.')

