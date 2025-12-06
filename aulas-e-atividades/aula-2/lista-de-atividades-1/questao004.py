# Questão 4

produto_valor = float(input('Informe o preço de um produto: '))
desconto = produto_valor * 0.5

if produto_valor >= 100:
    print(f'Com desconto, o produto irá custar R${desconto}.')
else:
    print(f'Infelizmente esse produto não possui desconto. O valor total é R${produto_valor}.')