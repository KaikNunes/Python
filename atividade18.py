vet1 = []
vet2 = []

print("Digite 10 números para completar o Vetor 1")
for i in range(10):
    vet1.append(int(input("Número: ")))

print("\nDigite 10 números para completar o Vetor 2")
for i in range(10):
    vet2.append(int(input("Número: ")))

res = vet1 + vet2
res[::2] = vet1
res[1::2] = vet2

print("\nVetor 3: ", res)