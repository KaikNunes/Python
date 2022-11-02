n = int(input("Qual mês deseja encontrar? "))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("Número total de coelhos: 1")
else:
    for i in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        i += 1
    print("Número total de coelhos: ", termo)