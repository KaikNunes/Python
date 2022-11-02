num = int(input("Digite um numero: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print (i, end="")
    num = num + 1
    print ("\r")