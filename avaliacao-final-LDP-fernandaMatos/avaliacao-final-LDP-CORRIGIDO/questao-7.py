# Questão 7

"""
Como respondi na prova:

media_enem = int(input("Qual foi a sua média no ENEM 2025: "))
curso_mensalidade = 1000

if media_enem  <= 450:
    desconto = 20/100
    mensalidade_total = 1000 - (curso_mensalidade * desconto)
    print(f"Sua media no ENEM 2025 é {media_enem}. O desconto aplicado será de {desconto:.2%}. O valor total da mensalidade será R${mensalidade_total}.")

elif 451 <= media_enem <= 550:
    desconto = 30/100
    mensalidade_total = 1000 - (curso_mensalidade * desconto)
    print(f"Sua media no ENEM 2025 é {media_enem}. O desconto aplicado será de {desconto:.2%}. O valor total da mensalidade será R${mensalidade_total}.")
    
elif 551 <= media_enem <= 600:
    desconto = 35/100
    mensalidade_total = 1000 - (curso_mensalidade * desconto)
    print(f"Sua media no ENEM 2025 é {media_enem}. O desconto aplicado será de {desconto:.2%}. O valor total da mensalidade será R${mensalidade_total}.")

elif 601 <= media_enem <= 650:
    desconto = 40/100
    mensalidade_total = 1000 - (curso_mensalidade * desconto)
    print(f"Sua media no ENEM 2025 é {media_enem}. O desconto aplicado será de {desconto:.2%}. O valor total da mensalidade será R${mensalidade_total}.")

elif 651 <= media_enem <= 700:
    desconto = 50/100
    mensalidade_total = 1000 - (curso_mensalidade * desconto)
    print(f"Sua media no ENEM 2025 é {media_enem}. O desconto aplicado será de {desconto:.2%}. O valor total da mensalidade será R${mensalidade_total}.")
        
else:
    print(f"Sua media no ENEM 2025 é {media_enem}. O desconto aplicado será de 100%. Portanto, você não precisará pagar mensalidade.")

"""

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