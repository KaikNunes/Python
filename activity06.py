# Recebendo turno do usuário
turno = str(input("Em qual turno você estuda?, (M para Matutino, V para Vespertino e N para Noturno): "))

# Definindo turno como letra maiúscula
turno = turno.upper()

# Condicional caso
match turno:
    case "M":
        print("Bom Dia!")
    case "V":
        print("Boa Tarde!")
    case "N":
        print("Boa Noite!")