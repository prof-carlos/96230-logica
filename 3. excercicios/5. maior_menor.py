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

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else: 
    maior = segundo_numero
    menor = primeiro_numero

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
