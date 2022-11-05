n = int(input("Escreva um número a ser fatorado: "))

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(f"{n}! = {fatorial(n)}")