# Desafio 1: Cofre com meta

# Crie um programa que simule um cofrinho. O usuário informa quanto quer juntar.
# Depois, dentro do while, o programa vai pedindo valores a serem adicionados, até a meta ser alcançada.
# Quando a meta for alcançada exiba uma mensagem avisando o usuário, e o informe sua meta e qual foi o valor total que ele juntou.

meta = float(input('Informe o valor da meta: R$'))
saldo = 0

while saldo < meta:
    valor = float(input('Digite o valor a ser adicionado ao cofre: R$'))
    saldo += valor
    print(f'Saldo atual: R${saldo}')

print('Parabéns! A meta foi atingida!')
print(f'O valor da meta era R${meta:.2f}')
print(f'Valor final depositado: R${saldo:.2f}')