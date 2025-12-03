## Operadores relacionais ##

# Listagem 3.2 - Exemplo de uso de operadores relacionais

a = 1 # a recebe 1
b = 5 # b recebe 5
c = 2 # c recebe 2
d = 1 # d recebe 1

print(a == b) # a é igual a b? Falso
print(b > a) # b é maior que a? Verdadeiro
print(a < b) # a é menor que b? Verdadeiro
print(a == d) # a é igual a d? Verdadeiro
print(b >= a) # b é maior ou igual a a? Verdadeiro
print(c <= b) # c é menor ou igual a b? Verdadeiro
print(d != a) # d é diferente de a? Falso
print(d != b) # d é diferente de b? Verdadeiro

# Listagem 3.3 - Exemplo de uso de operadores relacionais com variáveis do tipo lógico

nota = 8
média = 7

aprovado = nota > média 
print(aprovado)

# Exercício 3.2

a = 4
b = 10
c = 5.0
d = 1
f = 5

print(a == c) # a é igual a c? False
print(a < b) # a é menor que c? True
print(a > b) # a é maior que b? False
print(d == f) # a é igual a f? False
print(a == b) # a é igual a b? False
print(c < d) # c é menor que d? False
print(b > a) # b é maior que a? True
print(c >= f) # c é maior ou igual a f? True
print(f >= c) # f é maior ou igual a c? True
print(c <= c) # c é menor ou igual a c? True
print(c <= f) # c é menor ou igual a f? True

## Operadores lógicos ##
# Exemplo 1 — Checar idade

idade = 20
maior_de_idade = idade >= 18

if maior_de_idade:
    print("Pode entrar!")

# Exemplo 2 — Usando AND

sol = True
feriado = False

if sol and feriado:
    print("Vamos ao parque!")
else:
    print("Hoje não dá.")

# Exemplo 3 — Usando OR

tem_bolo = False
tem_biscoito = True

if tem_bolo or tem_biscoito:
    print("Hora do lanche!")

# Exemplo 4 — Usando NOT

chovendo = True

if not chovendo:
    print("Dá para sair!")
else:
    print("Melhor ficar em casa.")
