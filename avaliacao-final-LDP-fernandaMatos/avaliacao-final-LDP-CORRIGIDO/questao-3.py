# Questão 3

"""
Como respondi na prova:

cursos_superiores = ['Medicina', 'Direito', 'Engenharia']
print(f"Lista de cursos superiores mais desejados pelos candidatos: \n{cursos_superiores}")

cursos_superiores.sort()
print(f"Lista de cursos superiores mais desejados pelos candidatos em ordem alfabética: \n{cursos_superiores}")

"""

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