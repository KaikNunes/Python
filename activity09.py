# Recebendo os valores
nota1 = float(input("Digite sua nota do 1° Bimestre: "))
nota2 = float(input("Digite sua nota do 2° Bimestre: "))
nota3 = float(input("Digite sua nota do 3° Bimestre: "))
nota4 = float(input("Digite sua nota do 4° Bimestre: "))

# Total de pontos anuais
totalAno = (nota1 + nota2 + nota3 + nota4)

# if, elif, else
if totalAno >=60:
    print("Parabéns! Você foi aprovado com {} pontos" .format(totalAno))

elif (totalAno >=40) and (totalAno <60):
    print("Que pena, você está de recuperação com {} pontos" .format(totalAno))

elif totalAno <40:
    print("Infelizmente você está reprovado com {} pontos" .format(totalAno))