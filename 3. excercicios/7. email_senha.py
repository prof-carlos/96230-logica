# Limpar o terminal.
import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário o login e a senha.
# Considere que os dados do usuário já estão cadastrados.
# Caso o login e senha estejam corretos, mostre a mensagem:
#  “Bem-vindo!”
# Caso contrário, mostre a mensagem: 
# “Login ou senha inválidos.”

login_cadastrado = "marta"
senha_cadastrada = "123"

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo")
else:
    print("Login ou senha inválidos!")
