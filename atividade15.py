bruto = float(input("Qual o seu salário bruto por hora? "))
horas = int(input("Quantas horas você trabalhou no mês? "))
total = bruto * horas

ir = total*0.11
inss = total*0.08
sindicato = total*0.05
liquido = (total-ir-inss-sindicato)

print("\nDesconto do Imposto de Renda: ", round(ir, 2))
print("Desconto do INSS: ", round(inss, 2))
print("Desconto do Sindicato:", round(sindicato,2))
print("Salário líquido: ", round(liquido,2))

