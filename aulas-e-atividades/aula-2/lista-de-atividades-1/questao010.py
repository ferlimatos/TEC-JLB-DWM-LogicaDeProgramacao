# Questão 10

# Velocidade Máxima
velocidade_carro = int(input('Informe a velocidade do carro em km/h: '))
print(f'A velocidade de seu carro é {velocidade_carro} km/h.')
print(f'A velocidade máxima permitida é 80 km/h.')

limite = 80

if velocidade_carro > limite:
    excesso = velocidade_carro - limite
    print('Você ultrapassou o limite máximo permitido e portanto, cometeu uma infração.')
    
    if excesso <= 10:
            print('Você cometeu uma infração leve. Receberá 3 pontos na carteira.')
    elif 11 <= excesso <= 20:
            print('Você cometeu uma infração média. Receberá 4 pontos na carteira.')
    else:
            print('Você cometeu uma infração grave. Receberá 7 pontos na carteira.')

else:
    print('Você está dentro do limite permitido. Portanto, não cometeu uma infração.')