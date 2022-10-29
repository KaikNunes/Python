matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for l in range(0,5):
    for c in range(0,5):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

n = int(input("Digite um número para verificação: "))
for l in range(5):
    for c in range(5):
        if matriz[l][c] == n:
            print("acertou")
        else:
            print("errou")
