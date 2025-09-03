import os
os.system("cls")

print("""
Código    Prato             Valor
  1       Picanha          R$ 25,00
  2       Lasanha          R$ 20,00
  3       Strogonoff       R$ 18,00
  4       Bife acebolado   R$ 15,00
  5       Pão com ovo      R$ 5,00      
""")

codigo = int(input("Digite o código do prato desejado: "))

match codigo:
    case 1:
        prato = "Picanha"
        preco = 25
    case 2:
        prato = "Lasanha"
        preco = 20
    case 3:
        prato = "Strogonoff"
        preco = 18
    case 4:
        prato = "Bife acebolado"
        preco = 15
    case 5:
        prato = "Pão com ovo"
        preco = 5
    case _:
        print("Opção inválida.")

print(f"Prato: {prato}")
print(f"Preço: {preco}")

print("Volte sempre!")
