print("Digite o número que deseja calcular")

print("0 = sair")
print("1 = tensão elétrica")
print("2 = resistência elétrica")
print("3 = corrente elétrica")
print("4 = resistência resistor")

formula = input("digite o número correspondente ao que você deseja descobrir: ")

while formula != "0":


    if formula == "1":
        resistencia = float(input("qual a resistência elétrica em volts? "))
        corrente = float(input("qual a corrente elétrica? "))
        tensao = resistencia * corrente
        print(" a tensão elétrica é", tensao, "V")

    elif formula == "2":
        tensao = float(input("qual a tensão elétrica em ohms? "))
        corrente = float(input("qual a corrente elétrica? "))
        resistencia = tensao / corrente
        print("a resistência elétrica é", resistencia, "Ω")

    elif formula == "3":
        tensao = float(input("qual a tensão elétrica em amperes? "))
        resistencia = float(input("qual a resistência elétrica? "))
        corrente = tensao / resistencia
        print("a corrente elétrica é", corrente, "A")

    elif formula == "4":
        tensaofonte = float(input("digite a tensão da fonte em ohms?"))
        tensaoled = float(input("digite a tensão do LED?"))
        correnteled = float(input("digite a corrente do LED?"))
        resistenciaresistor = (tensaofonte - tensaoled) / correnteled
        print(" a resistência do resistor é", resistenciaresistor)

    else:
        print("Essa opção é inválida.")

    print("")
    print("0 = sair")
    print("1 = tensão elétrica")
    print("2 = resistência elétrica")
    print("3 = corrente elétrica")
    print("4 = resistência resistor")

    formula = input("digite o número correspondente ao que você deseja descobrir: ")
