# Uso do while
resposta = "S"
while resposta == "S":

    # Recebendo informações do usuário
    operacao = str(input("Escolha a Operação que deseja fazer: Soma, Subtração, Multiplicação ou Divisão: "))
    n1 = int(input("Escolha primeiro número: "))
    n2 = int(input("Escolha segundo número: "))

    # Formatando como minúsculas
    operacao = operacao.lower()

    # Usando condicional para fazer as contas (if, elif, else)
    if operacao == 'soma':
        soma = (n1 + n2)
        print("Resultado: ", soma)

    elif operacao == "subtracao":
        subtracao = (n1 - n2)
        print("Resultado: ", subtracao)

    elif operacao == "multiplicacao":
        multiplicacao = (n1 * n2)
        print("Resultado: ", multiplicacao)

    elif operacao == "divisao":
        divisao = (n1 / n2)
        print("Resultado: ", divisao)

    else:
        print("Verifique os dados informados!")

    resposta = str(input("Deseja continuar usando a calculadora? "))
    resposta = resposta.upper() 

