# Exercício 3
# Encontrando o Extremo
# Crie uma lista com pelo menos 5 notas de alunos (use float). Use as funções auxiliares max() e min() para encontrar e imprimir a maior nota e a menor nota obtidas na lista.
# 

notas_alunos = []

for i in range(5):
  nota = float(input(f"Informe a nota do Aluno {i+1}: "))
  notas_alunos.append(nota)

maior_nota = max(notas_alunos)
menor_nota = min(notas_alunos)

# quais foram os alunos que obteve cada uma
indice_maior = notas_alunos.index(maior_nota)
indice_menor = notas_alunos.index(menor_nota)

print(f"Lista de notas: {notas_alunos}")
print(f"A maior nota da lista foi {maior_nota}, do Aluno {indice_maior+1}.")
print(f"A menor nota da lista foi {menor_nota}, do Aluno {indice_menor+1}.")
