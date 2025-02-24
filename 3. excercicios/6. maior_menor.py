# Limpar o terminal.
import os
os.system("clear")

# Elabore um algoritmo usando operações lógicas para solicitar ao usuário 2 
# números e escrever:
#
# Os 2 números informados.
# O maior número;
# O menor número; 

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")

if primeiro_numero == segundo_numero and primeiro_numero > segundo_numero:
    print("Os números são iguais.")
else:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

