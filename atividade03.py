# inserção dos números
n1 = input("Esrceva o primeiro número: ")
n2 = input("Escreva o segundo número: ")

# soma
soma = (int(n1)+int(n2))
print("\nO resultado da soma é: ", soma)

# subtração
subtracao = (int(n1)-int(n2))
print("O resultado da subtração é: ", subtracao)

# multiplicação comum
multiplicacao = (int(n1)*int(n2))
print("O resultado da multiplicação é: ", multiplicacao)

# exponenciação
exponenciacao = (int(n1)**int(n2))
print("O resultado da exponenciação é: ", exponenciacao)

# divisão comum
divisao = round(float(n1)/float(n2), 2)
print("O resultado da divisão é: ", divisao)

# divisão resto
resto = (float(n1)) % (float(n2))
print("O resultado da divisão resto é: ", resto)