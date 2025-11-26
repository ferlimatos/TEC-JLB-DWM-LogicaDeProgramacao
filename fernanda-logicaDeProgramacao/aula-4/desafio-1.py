# Desafio 1: Cofre com meta

meta = float(input('Informe o valor da meta: R$'))
saldo = 0

while saldo < meta:
    valor = float(input('Digite o valor a ser adicionado ao cofre: R$'))
    saldo += valor
    print(f'Saldo atual: R${saldo}')

print('Parabéns! A meta foi atingida!')
print(f'O valor da meta era R${meta:.2f}')
print(f'Valor final depositado: R${saldo:.2f}')