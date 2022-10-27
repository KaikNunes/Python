#definição das constantes
iphone = 2980.00
samsung = 2540.00
tablet = 1950.00
playstation = 2100.00
notebook = 2350.00

#declaração da quantidade pedida
qntIphone = int(input("O Iphone custa R${}, quantos você deseja comprar? ".format(iphone)))
qntSamsung = int(input("O Samsung custa R${}, quantos você deseja comprar? " .format(samsung)))
qntTablet = int(input("O Tablet custa R${}, quantos você deseja comprar? " .format(tablet)))
qntPlaystation = int(input("O Playstation 5 custa {}, quantos você deseja comprar? " .format(playstation)))
qntNotebook = int(input("O Notebook custa R${}, quantos você deseja comprar? " .format(notebook)))

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
