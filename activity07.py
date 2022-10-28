# Recebendo informações do usuário
numeroTabuada = int(input("Qual tabuada você quer? "))
numeroInicial = int(input("Digite qual primeiro múltiplo: "))
numeroFinal = int(input("Digite qual último multiplo: "))

# Repetição para
for i in range (numeroInicial, numeroFinal +1):
    print((numeroTabuada), "*", i, "=", i * numeroTabuada)
