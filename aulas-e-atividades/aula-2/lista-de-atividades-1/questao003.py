# Questão 3

n1 = float(input('Digite a nota da n1: '))
n2 = float(input('Digite a nota da n2: '))
n3 = float(input('Digite a nota da n3: '))
n4 = float(input('Digite a nota da n4: '))
media = (n1 + n2 + n3 + n4) / 4

if media >= 6.0:
    print(f'A sua média final é {media}. Parabéns, você está aprovado! 😍')
else:
    print(f'A sua média final é {media}. Infelizmente você não alcançou a média necessário. Você está reprovado.')
