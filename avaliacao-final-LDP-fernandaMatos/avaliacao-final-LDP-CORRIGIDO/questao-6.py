# Questão 6

"""
Como respondi na prova:

media_minima = 450

media_enem = int(input("Digite a sua média do ENEM 2025: "))
redacao = int(input("Digite sua nota da Redação do ENEM 2025: "))

if media_enem >= media_minima and redacao != 0:
    print(f"Sua média do ENEM 2025 é {media_enem} e sua nota na redação é {redacao}. Você está apto para se inscrever no ProUni.")

elif media_enem < media_minima and redacao != 0:
        print(f"Você atingiu a nota média do ENEM mas sua redação foi zero. Você NÃO ESTÁ apto para se inscrever no ProUni.")

else:
    redacao = 0
    print(f"Sua nota na redação do ENEM foi 0. Você não está apto para se inscrever no ProUni.")
"""

# Questão 6 - Corrigida

media_minima = 450

media_enem = int(input("Digite a sua média do ENEM 2025: "))
redacao = int(input("Digite sua nota da Redação do ENEM 2025: "))

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