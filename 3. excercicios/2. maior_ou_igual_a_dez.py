# Limpar o terminal.
import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário um valor e escrever a mensagem: 
# “É MAIOR QUE 10!”. 
# se o valor lido for maior que 10, caso contrário escrever:
# “NÃO É MAIOR QUE 10!”
# Verifique se o número digitado é igual a 10, caso seja, escreva a mensagem: 
# “O número é igual a 10!”#

numero = int(input("Digite um número: "))

if numero == 10:
    print("É IGUAL A 10!")
elif numero > 10:
    print("É MAIOR QUE 10!")
else: 
    print("NÃO É MAIOR QUE 10!")
