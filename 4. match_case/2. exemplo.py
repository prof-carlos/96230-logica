# Limpar o terminal.
import os
os.system("clear")

# Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante 
# para uma pessoa. 
# A pessoa vai escolher o prato desejado digitando o código do prato.
# Após escolher o prato, o algoritmo deve mostrar o nome e valor do prato escolhido.

# Entrada
opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanha \t\t R$ 20,00    
3 \t Strogonoff \t\t R$ 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00

Digite a opção desejada:
"""))

# Processamento
# Saída
match opcao:
    case 1:
        print("Picanha - R$ 25,00")
    case 2:
        print("Lasanha - R$ 20,00")
    case 3:
        print("Strogonoff - R$ 18,00")
    case 4:
        print("Bife acebolado - R$ 15,00")
    case 5:
        print("Pão com ovo - R$ 5,00")
    case _:
        print("Opção inválida.")

