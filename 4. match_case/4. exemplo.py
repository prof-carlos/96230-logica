# Limpar o terminal.
import os
os.system("clear")

# Desenvolva um programa que receba como entrada um número inteiro que 
# represente um dos 7 dias da semana e imprima na tela se esse dia é útil, 
# final de semana ou inválido.
# Considere que Domingo é o dia 1 e Sábado o dia 7.

# Entrada
dia = int(input("Digite um número para o dia da semana: "))

# Processamento
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Opção inválida")
