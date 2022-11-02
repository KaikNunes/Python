lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(20):
    lista[i] = str(input("Digite seu nome: "))

def alfabetica():
    lista.sort()
    print("\nNomes organizados: ", lista)

alfabetica()

