# Exercício 10

# Crie um algoritmo que peça para o usuário digitar o valor do produtos que ele está comprando até que ele digite 0 para parar. Ao final, imprima a quantidade de itens da compra do usuário, o valor final, e a forma de pagamento que ele poderá optar, tendo as seguintes condições:

# a. Compras de valor inferior a R$ 50 só poderão ser pagas via débito ou pix;
# b. Compras entre R$ 50 e R$ 100 poderão ser pagas via cartão de crédito em 1 vez;
# c. Compras acima de R$ 100 podem ser parceladas em até 2 vezes;
# d. Compras acima de R$ 200 podem ser parceladas em até 3 vezes.

'''Minha resposta:'''

quantidade_itens = 0
valor_total = 0

while True:
    valor = float(input("Digite o valor do produto (0 para encerrar): "))
    if valor == 0:
        break
    quantidade_itens += 1
    valor_total += valor

print(f"\nQuantidade de itens: {quantidade_itens}")
print(f"Valor total da compra: R$ {valor_total:.2f}")

if valor_total < 50:
    print("Forma de pagamento: débito ou pix.")
elif valor_total <= 100:
    print("Forma de pagamento: cartão de crédito em 1 vez.")
elif valor_total <= 200:
    print("Forma de pagamento: cartão de crédito em até 2 vezes.")
else:
    print("Forma de pagamento: cartão de crédito em até 3 vezes.")

