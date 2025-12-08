# Exercício 10
# Fusão e Ordenação Segura (Sorted)
# Você tem duas listas de notas: primeiro_bimestre = [7.5, 8.0, 6.0] e segundo_bimestre = [9.0, 6.5, 7.0]. 
# a. Crie uma terceira lista que contenha todos os elementos das duas listas. 
# b. Use a função sorted() para criar uma nova lista chamada notas_finais_ordenadas com todas as notas em ordem crescente, garantindo que as listas originais (primeiro_bimestre e segundo_bimestre) não sejam alteradas. 
# c. Imprima todas as três listas para comprovar que as listas originais não foram modificadas.

# Listas originais
primeiro_bimestre = [7.5, 8.0, 6.0]
segundo_bimestre = [9.0, 6.5, 7.0]

# Nova lista com todos os elementos das duas listas originais
nova_lista = primeiro_bimestre + segundo_bimestre
print(f"Nova lista: {nova_lista}")

# Nova lista das notas finais ordenadas
notas_lista_ordenada = sorted(primeiro_bimestre+segundo_bimestre)
print(f"\nNova lista das notas finais ordenadas: {notas_lista_ordenada}")

# Impressao das três listas
print("\nComprovando que as listas não foram alteradas:")
print(f"Lista 'primeiro_bimestre' original: {primeiro_bimestre}")
print(f"Lista 'segundo_bimestre' original: {segundo_bimestre}")
print(f"Lista 'notas_finais_ordenadas': {notas_lista_ordenada}")
