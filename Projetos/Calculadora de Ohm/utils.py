print("Digite o número que deseja calcular de acordo com o menu.")

def menu():
    print("Menu:")
    print("0 = sair")
    print("1 = tensão elétrica")
    print("2 = resistência elétrica")
    print("3 = corrente elétrica")
    print("4 = resistência resistor")

def solicita_numero():
    while True:
        try:
            numero = int(input("digite o número correspondente ao que você deseja descobrir: "))
            if numero >= 0 and numero <= 4:
                return numero
            else:
                print("Digite apenas números entre 0 e 4")
        except ValueError:
            print("Essa resposta está inválida, digite apenas números.")

def solicita_tensao():
    while True:
        try:
            tensao = float(input("Digite a tensão elétrica em Volts:"))
            if tensao >= 0:
                return tensao
        except ValueError:
            print("Valor inválido, tente novamente.")


def solicita_resistencia():
    while True:
        try:
            resistencia = float(input("Digite a resistência elétrica em Ω:"))
            if resistencia >= 0:
                return resistencia
        except ValueError:
            print("Valor inválido, tente novamente.")

def solicita_corrente():
    while True:
        try:
            corrente = float(input("Digite a corrente elétrica em A"))
            if corrente >= 0:
                return corrente
        except ValueError:
            print("Valor inválido, tente novamente.")


def solicita_resistencia_resistor():
    while True:
        try:
            tensao_fonte = float(input("Digite a tensão da fonte em Volts:"))
            if tensao_fonte >= 0:
                return tensao_fonte
        except ValueError:
            print("Valor inválido, tente novamente.")


def tensao_conta(resistencia,corrente):
    return resistencia * corrente


def resistencia_conta(tensao,corrente):
    return tensao / corrente


def corrente_conta(tensao,resistencia):
    return tensao / resistencia


def resistencia_resistor_conta(tensao, tensao_fonte, corrente):
    return (tensao - tensao_fonte) / corrente

def exibir_resultado(numero):
    print("Resultado:")

    if numero == 1:
        print("Tensão elétrica")
        resistencia1 = solicita_resistencia()
        corrente1 = solicita_corrente()
        print(tensao_conta(resistencia1,corrente1))

    elif numero == 2:
        print("Resistência elétrica")
        tensao1 = solicita_tensao()
        resistencia1 = solicita_resistencia()
        print(resistencia_conta(tensao1,resistencia1))

    elif numero == 3:
        print("Corrente elétrica")
        tensao1 = solicita_tensao()
        resistencia1 = solicita_resistencia()
        print(corrente_conta(tensao1,resistencia1))

    elif numero == 4:
        print("Resistência resistor")
        tensao1 = solicita_tensao()
        tensao_fonte1 = solicita_resistencia_resistor()
        corrente1 = solicita_corrente()
        print(resistencia_resistor_conta(tensao1,tensao_fonte1,corrente1))

menu()
print("")
escolha_final = solicita_numero()
exibir_resultado(escolha_final)