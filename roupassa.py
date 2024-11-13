# Define os valores da compra e do desconto
valor_compra = 350.00
desconto = 10  # em porcentagem

# Calcula o valor do desconto
valor_desconto = (desconto / 100) * valor_compra

# Calcula o valor final após aplicar o desconto
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print(f"Olá Ana Beatriz. Em DEZEMBRO você fez uma compra no valor de R$ {valor_compra:.2f} e ganhou um desconto de {desconto}% em sua próxima compra.")
print(f"Use o cupom ANA1O para obter R$ {valor_desconto:.2f} de desconto.")
print(f"O valor final da sua próxima compra será R$ {valor_final:.2f}.")

# Testando a execução do código
print("\n--- Teste da execução do código ---")


