# Limpar o terminal.
import os
os.system("clear")

# Elabore um algoritmo usando operações lógicas para informar se uma 
# pessoa é obrigada a votar.
# Considere que a regra é que menores de 18 e maiores que 65 
# não são obrigados a votar.


# Entrada
idade = int(input("Digite sua idade: "))

# Processamento
# Opção 1.
# if idade < 18 or idade > 65:
#     resultado = "Não é obrigado a votar."
# else:
#     resultado = "Voto obrigatório."

# Opção 2.
if idade >= 18 and idade <= 65:
    resultado = "Voto obrigatório."
else:
    resultado = "Não é obrigado a votar."

# Saída
print(f"\nResultado: {resultado}")