# Questão 5

# Dados de Entrada
linguagens_tecnologias = int(input("Digite sua nota de Linguagens, Códigos e suas Tecnologias: "))
matematica_tecnologias = int(input("Digite sua nota de Matemática e suas Tecnologias: "))
ciencia_natureza = int(input("Digite sua nota de Ciências da Natureza e suas Tecnologias: "))
ciencia_humana = int(input("Digite sua nota de Ciências Huamanas e suas Tecnologias: "))
redacao = int(input("Digite sua nota de Redação: "))

# Cálculo da média
media_enem = (linguagens_tecnologias + matematica_tecnologias + ciencia_natureza + ciencia_humana + redacao) / 5

# Dados de Saída
print(f"Sua nota de Linguagens, Códigos e suas Tecnologias é {linguagens_tecnologias}.")
print(f"Sua nota de Matemática e suas Tecnologias é {matematica_tecnologias}.")
print(f"Sua nota de Ciências da Natureza e suas Tecnologias é {ciencia_natureza}.")
print(f"Sua nota de Ciências Huamanas e suas Tecnologias é {ciencia_humana}.")
print(f"Sua nota de Redação é {redacao}.")
print(f"Sua pontuação final do ENEM é {media_enem}.")
