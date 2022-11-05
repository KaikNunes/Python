preco = float(input("Preço da unidade do pão R$ "))

print("Tabela de preços")

for i in range(1, 51):
    print(f"{i} - R$ {preco*i:.2f}")
