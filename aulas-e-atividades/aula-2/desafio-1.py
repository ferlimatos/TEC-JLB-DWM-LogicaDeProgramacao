# Desafio 1

# Escreva um programa que leia a nota de um simulado do ENEM.
# Se a nota for maior ou igual a 700, mostre uma mensagem parabenizando e dizendo que a pessoa está no caminho certo para passar
# Se a nota estiver entre 500 e 699, diga que precisa revisar alguns conteúdos
# Se a nota for abaixo de 500, avise que precisa reforçar os estudos urgentemente

nota = float(input("Digite a nota do seu simulado do ENEM: "))

if nota >= 700:
  print("Parabéns! Você está no caminho certo para conquistar a vaga!")
elif nota >= 500:
  print("Atenção! Vale a pena revisar alguns conteúdos para melhorar ainda mais seu desempenho.")
else:
  print("Estude com mais foco! Ainda dá tempo de reforçar e recuperar o aprendizado.")