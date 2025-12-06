## Conceito Básico e Estrutura

# Uma lista é uma coleção que guarda vários valores em uma única variável. Elas são a forma mais comum e flexível de armazenar coleções de dados na linguagem Python.
 # Criação: Para criar uma lista, você usa o sinal de igual (=) e coloca os itens entre colchetes ([]), separados por vírgulas.

frutas = ["maçã", "banana", "uva"] # lista de strings
numeros = [10, 20, 30, 40] # lista de números
vazia = [] # lista vazia
print(frutas, numeros, vazia)

## Acessando e Modificando Elementos

# Acesso por Posição (Índice)
# Para acessar um item específico na lista, você referencia o número da sua posição (índice) entre colchetes.
  # A contagem de posições sempre começa no 0 (zero).
print(frutas[0])

# Modificação de Elementos
# Como as listas são mutáveis, você pode alterar o valor de um item indicando a posição dele e fazendo a substituição.

# Altera a primeira posição (índice 0) de "maçã"
frutas [0] = "abacate"
print(frutas) 
# A lista agora é: ['abacate', 'banana', 'uva']

## Adicionando Elementos
# Você pode aumentar o tamanho da sua lista de duas maneiras principais:
frutas = ["abacate", "banana", "maça", "pera", "uva", "morango", "laranja"]
frutas.sort()
print(frutas)

## Removendo Elementos
# Existem duas formas comuns de remover itens de uma lista:
frutas.remove("uva") # list.remove("valor") - Remove o primeiro item que corresponde ao valor especificado.
del frutas[0] # del list[posição] - Remove o item na posição (índice) determinada.

## Ordenando Listas (Sort e Sorted)
# Para colocar uma lista em ordem (alfabética para strings ou numérica para números), você pode usar o método .sort() ou a função sorted().
frutas.sort() # list.sort() - Modifica a lista original (in-place).
legumes_ordenados = sorted(legumes) # sorted(list) - Cria e retorna uma nova lista ordenada, sem alterar a lista original.
sorted(numeros, reverse=True) # Ordem Decrescente - Use o argumento reverse=True com sorted().

## Funções de Análise Rápida (Max e Min)
# As funções max() e min() são úteis para encontrar o maior e o menor elemento de uma lista:
  ## Com números: Retorna o maior e o menor valor numérico, respectivamente.
  # Exemplo: max([1, 5, 35]) retorna 35.
  ## Com números: Retorna o maior e o menor valor numérico, respectivamente.
  ## Com strings: Retorna o elemento que seria o último (max) ou o primeiro (min) em ordem alfabética.
  # Exemplo: max(["abacate", "uva"]) retorna "uva".

frutas = ["abacate", "banana", "maça", "pera", "uva"]
maior_fruta = max(frutas)
print(maior_fruta)

numeros = [1,5,6,9,18,35]
numero_maior = max(numeros)
print(numero_maior)
#OU
print(f'{min(numeros)}')
