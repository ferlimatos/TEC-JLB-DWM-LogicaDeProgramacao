nome_correto = 'Fernanda'
tentativas = input('Informe um nome: ')

while tentativas != nome_correto:
    print('Nome incorreto! Tente novamente.')
    tentativas = input('Informe um novo nome: ')

print('Nome correto! Acesso liberado!')