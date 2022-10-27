#definição das constantes
iphone = 2980.00
samsung = 2540.00
tablet = 1950.00
playstation = 2100.00
notebook = 2350.00

#declaração da quantidade pedida
qntIphone = int(input("Quantos IPhone's você deseja comprar? "))
qntSamsung = int(input("Quantos Samsung's você deseja comprar? "))
qntTablet = int(input("Quantos Tablet's você deseja comprar? "))
qntPlaystation = int(input("Quantos Playstation's 5 você deseja comprar? "))
qntNotebook = int(input("Quantos Notebook's você deseja comprar? "))

#total comum
total = (qntIphone*iphone) + (qntSamsung*samsung) + (qntTablet*tablet) + (qntPlaystation*playstation) + (qntNotebook*notebook)
print("O valor total da sua compra é: R$ {}" .format(total))

#parcelado em 3x
parcela3 = round(total/3, 2)
print("O valor parcelado em 3x é: R$ {}" .format(parcela3))

#parcelado em 6x com acréscimo
parcela6 = round((total*1.05)/6, 2)
print("O valor parcelado em 6x é: R$ {}" .format(parcela6))

#total com desconto
totalDesconto = round(total-(total*0.1), 2)
print("O valor à vista com desconto é: R$ {}" .format(totalDesconto))
