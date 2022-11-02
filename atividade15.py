bruto = float(input("Qual o seu salário bruto por hora? "))
horas = int(input("Quantas horas você trabalhou no mês? "))
total = bruto * horas

ir = total*0.11
inss = total*0.08
sindicato = total*0.05
liquido = (total-ir-inss-sindicato)

print("\nSalário bruto: R${}" .format (round(total, 2)))
print("Desconto do Imposto de Renda: R${}" .format(round(ir, 2)))
print("Desconto do INSS: R${}" .format(round(inss, 2)))
print("Desconto do Sindicato: R${}" .format(round(sindicato,2)))
print("Salário líquido: R${}" .format(round(liquido,2)))

