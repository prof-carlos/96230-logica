# Limpar o terminal.
import os
os.system("clear")

# Entrada
valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input(""" 
1 - A vista
2 - A prazo
Digite a forma de pagamento: """))

match forma_de_pagamento:
    case 1:
        # Aplicando desconto de 10%.
        desconto = valor_produto * 0.10
    case 2:
        ...
    case _:
        print("Opção inválida.")



