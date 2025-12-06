# Exercício 4

# Peça ao usuário para acertar o seu nome e use while para repetir a pergunta até ele acertar.

nome_correto = 'Fernanda'
tentativas = input('Informe um nome: ')

while tentativas != nome_correto:
    print('Nome incorreto! Tente novamente.')
    tentativas = input('Informe um novo nome: ')

print('Nome correto! Acesso liberado!')