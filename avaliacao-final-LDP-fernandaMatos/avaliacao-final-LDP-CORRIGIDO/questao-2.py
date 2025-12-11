# Questão 2

email = "aluno@gmail.com"
senha = "123456"

login_email = input("Digite seu e-mail: ")
login_senha = input("Digite sua senha: ")

while login_email != email or login_senha != senha:
    print('Dados incorretos! Tente novamente.')
    login_email = input("Informe um novo e-mail: ")
    login_senha = input("Informe uma nova senha: ")

print("Acesso liberado!")
