# Questão 1
print("=== Questão 1 ====")

nome_completo = input("Informe seu nome completo: ")
cadastro_único = int(input("Digite seu número de CPF (sem ponto ou traço): "))
email = input("Informe seu endereço de e-mail: ")
senha = (input("Digite sua senha: "))

print(f"Cadastro para o ENEM 2025 concluído com sucesso. Seus dados de inscrição são: \nNome completo: {nome_completo}\nCPF: {cadastro_único}\nE-mail: {email}\nSenha: {senha}")

# Questão 2
print("\n=== Questão 2 ====")

login_email = input("Digite seu e-mail: ")
login_senha = input("Digite sua senha: ")

while login_email != email or login_senha != senha:
    print('Dados incorretos! Tente novamente.')
    login_email = input("Informe um novo e-mail: ")
    login_senha = input("Informe uma nova senha: ")

print("Acesso liberado!")

# Questão 3
print("\n=== Questão 3 ====")

cursos_superiores = []

curso1 = input("Digite o nome do 1º curso superior desejado: ")
curso2 = input("Digite o nome do 2º curso superior desejado: ")
curso3 = input("Digite o nome do 3º curso superior desejado: ")

cursos_superiores.append(curso1)
cursos_superiores.append(curso2)
cursos_superiores.append(curso3)

print(f"Lista de cursos superiores mais desejados pelos candidatos: \n{cursos_superiores}")

cursos_superiores.sort()

print(f"Lista de cursos superiores mais desejados pelos candidatos em ordem alfabética: \n{cursos_superiores}")

# Questão 4
print("\n=== Questão 4 ====")

print(f"Lista de cursos superiores mais desejados pelos candidatos: \n{cursos_superiores}")

cursos_superiores.append('Engenharia de Software')

print(f"Lista ATUALIZADA de cursos superiores mais desejados pelos candidatos: \n{cursos_superiores}")

# Questão 5
print("\n=== Questão 5 ====")

linguagens_tecnologias = float(input("Digite sua nota de Linguagens, Códigos e suas Tecnologias: "))
matematica_tecnologias = float(input("Digite sua nota de Matemática e suas Tecnologias: "))
ciencia_natureza = float(input("Digite sua nota de Ciências da Natureza e suas Tecnologias: "))
ciencia_humana = float(input("Digite sua nota de Ciências Huamanas e suas Tecnologias: "))
redacao = float(input("Digite sua nota de Redação: "))

media_enem = (linguagens_tecnologias + matematica_tecnologias + ciencia_natureza + ciencia_humana + redacao) / 5

print(f"Sua nota de Linguagens, Códigos e suas Tecnologias é {linguagens_tecnologias}.")
print(f"Sua nota de Matemática e suas Tecnologias é {matematica_tecnologias}.")
print(f"Sua nota de Ciências da Natureza e suas Tecnologias é {ciencia_natureza}.")
print(f"Sua nota de Ciências Huamanas e suas Tecnologias é {ciencia_humana}.")
print(f"Sua nota de Redação é {redacao}.")
print(f"Sua pontuação final do ENEM é {media_enem}.")

# Questão 6
print("\n=== Questão 6 ====")

media_minima = 450.00

media_enem = float(input("Digite a sua média do ENEM 2025: "))
redacao = float(input("Digite sua nota da Redação do ENEM 2025: "))

if media_enem >= media_minima and redacao != 0:
    print(f"Sua média do ENEM 2025 é {media_enem} e sua nota na redação é {redacao}.")
    print("Você está APTO para se inscrever no ProUni.")

else:
    print(f"Sua média do ENEM 2025 é {media_enem} e sua nota na redação é {redacao}.")
    print("Você NÃO está apto para se inscrever no ProUni. Motivo(s):")
    
    if media_enem < media_minima:
        print(f"A sua média ({media_enem} pontos) está abaixo da média mínima exigida de {media_minima} pontos.")

    if redacao == 0:
            print("  - Você zerou a redação do ENEM.")

# Questão 7
print("\n=== Questão 7 ====")

# Questão 7

media_enem = float(input("Qual foi a sua média no ENEM 2025: "))
curso_mensalidade = 1000.00
desconto_percentual = 0.0
bolsa_faixa = ""

if media_enem <= 450:
    desconto_percentual = 0.20 # 20%
    bolsa_faixa = "Até 450 (20% de bolsa)"
elif 451 <= media_enem <= 550:
    desconto_percentual = 0.30 # 30%
    bolsa_faixa = "De 451 a 550 (30% de bolsa)"
elif 551 <= media_enem <= 600:
    desconto_percentual = 0.35 # 35%
    bolsa_faixa = "De 551 a 600 (35% de bolsa)"
elif 601 <= media_enem <= 650:
    desconto_percentual = 0.40 # 40%
    bolsa_faixa = "De 601 a 650 (40% de bolsa)"
elif 651 <= media_enem <= 700:
    desconto_percentual = 0.50 # 50%
    bolsa_faixa = "De 651 a 700 (50% de bolsa)"
else: # 701 ou mais
    desconto_percentual = 1.00 # 100%
    bolsa_faixa = "701 ou mais (100% de bolsa)"

valor_desconto_mensal = curso_mensalidade * desconto_percentual
mensalidade_com_desconto = curso_mensalidade - valor_desconto_mensal
economia_anual = valor_desconto_mensal * 12

print("\nResultado da Bolsa de Estudos:")
print(f"Sua média no ENEM é: {media_enem}")
print(f"Sua faixa de desconto é: {bolsa_faixa}")

print(f"\nDetalhes da Mensalidade:")
print(f"Mensalidade sem desconto: R$ {curso_mensalidade:.2f}")
print(f"Desconto Mensal Aplicado: R$ {valor_desconto_mensal:.2f} ({desconto_percentual:.0%})")
print(f"Mensalidade com desconto: R$ {mensalidade_com_desconto:.2f}")
print(f"Economia ao final do primeiro ano: R$ {economia_anual:.2f}")