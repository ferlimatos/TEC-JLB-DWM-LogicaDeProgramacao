# Questão 9

compra_valor = float(input('Informe o valor de sua compra: R$'))

if compra_valor >= 200:
    if compra_valor >= 500:
        print(f'Parabéns, você ganhou um frete grátis e um brinde!')
    else:
        print('Parabéns, você ganhou um frete grátis.')
    frete = 0
    
else:
    if compra_valor >50:
        frete = 10

    else:
        frete = 20

valor_total = compra_valor + frete

print(f'O valor do frete é de R${frete}. Portanto, o valor total que precisa ser pago é R${valor_total}')





