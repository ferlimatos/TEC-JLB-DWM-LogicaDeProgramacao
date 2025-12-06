# Questão 8

peso = float(input('Qual o seu peso?' ))
altura = float(input('Qual é a sua altura?' ))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc}. Cuidado, você está abaixo do peso ideal.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC é {imc}. Você está em seu peso ideal.')
else:
    print(f'Seu IMC é {imc}. Cuidado, você está acima do peso ideal.')