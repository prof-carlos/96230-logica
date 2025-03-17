import os

os.system("cls || clear")

print("SOMANDO NÚMEROS:")
soma = 0
for i in range(5):
   nota = int(input(f"Digite um número: "))
#    soma = soma + nota
   soma += nota

print()
print(f"Soma: {soma}")

print("\nFIM DO PROGRAMA")