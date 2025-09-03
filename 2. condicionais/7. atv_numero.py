import os
os.system("cls")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a primeira nota: "))

media = (primeira_nota + segunda_nota) / 2

if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Média: {media}")
print(f"Resultado: {resultado}")