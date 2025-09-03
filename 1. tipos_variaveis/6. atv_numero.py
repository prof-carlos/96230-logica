import os
os.system("cls")

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
