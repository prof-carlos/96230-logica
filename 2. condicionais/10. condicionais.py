import os
os.system("cls")

valor_produto = float(input("Digite o valor do produto: "))

print("""
1 - À vista
2 - À prazo      
""")

forma_de_pagamento = int(input("Digite a forma de pagamento: "))

match forma_de_pagamento:
    case 1:
        # Obtendo o valor do desconto de 10%.
        desconto = valor_produto * 0.10
        valor_com_desconto = valor_produto - desconto

        print(f"\nValor do produto: R$ {valor_produto}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto}")
        print(f"Total a pagar: R$ {valor_com_desconto}")
    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
            valor_da_parcela = valor_produto / quantidade_parcelas

            print(f"\nValor do produto: R$ {valor_produto}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {quantidade_parcelas}")
            print(f"Valor por parcela: R$ {valor_da_parcela:.2f}")
            print(f"Total a pagar: R$ {valor_produto}")
        else:
            print("Número de parcelas inválida.")
    case _: 
        print("Forma de pagamento inválida.")

print("Volte sempre!")
