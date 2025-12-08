# Exercício 7
# Contagem com Índices
# Crie a lista de times: ['Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians']. 
# a. Use a função enumerate dentro de um laço for para percorrer a lista. 
# b. Imprima cada time junto com o seu índice, no formato: Índice [X]: Time.

times_futebol = ['Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians']
print(f"Lista de times inicial: \n{times_futebol}")

for index, time in enumerate(times_futebol, start=1):
  print(f"Lista de times com seu Índice: Índice: {index}, Time: {time}")
