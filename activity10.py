# Recebendo notas das provas
prova1 = float(input("Digite sua nota da prova do 1° Bimestre: "))
prova2 = float(input("Digite sua nota da prova do 2° Bimestre: "))
prova3 = float(input("Digite sua nota da prova do 3° Bimestre: "))
prova4 = float(input("Digite sua nota da prova do 4° Bimestre: "))

# Recebendo notas dos trabalhos
trabalho1 = float(input("\nDigite sua nota do trabalho do 1° Bimestre: "))
trabalho2 = float(input("Digite sua nota do trabalho do 2° Bimestre: "))
trabalho3 = float(input("Digite sua nota do trabalho do 3° Bimestre: "))
trabalho4 = float(input("Digite sua nota do trabalho do 4° Bimestre: "))

# Cálculo das médias
media1 = (prova1 + trabalho1)/2
media2 = (prova2 + trabalho2)/2
media3 = (prova3 + trabalho3)/2
media4 = (prova4 + trabalho4)/2

print("\nSua média do 1° Bimestre foi: ", media1)
print("Sua média do 2° Bimestre foi: ", media2)
print("Sua média do 3° Bimestre foi: ", media3)
print("Sua média do 4° Bimestre foi: ", media4)

# Cálculo dos totais
total1 = (prova1 + trabalho1)
total2 = (prova2 + trabalho2)
total3 = (prova3 + trabalho3)
total4 = (prova4 + trabalho4)
totalAno = total1 + total2 + total3 + total4

# if, elif, else
if totalAno >=60:
    print("Parabéns! Você foi aprovado com {} pontos" .format(totalAno))

elif (totalAno >=40) and (totalAno <60):
    print("Que pena, você está de recuperação com {} pontos" .format(totalAno))

elif totalAno <40:
    print("Infelizmente você está reprovado com {} pontos" .format(totalAno))
