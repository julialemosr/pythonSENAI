#Crie uma função que receba dois parâmetros que serão o peso e a altura de uma pessoa e retorne seu IMC.
#IMC = peso / (altura x altura)
#Depois crie outra função que receba um numero como parâmetro que será o IMC e retorne a classificação.

print("Digite sua altura e seu peso para saber seu IMC e sua classificação")
print("")


def solicita_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros: "))
            return altura
        except ValueError:
            print("Essa resposta é inválida, tente novamente")


def solicita_peso():
    while True:
        try:
            peso = float(input("Digite sua peso em Kg: "))
            return peso
        except ValueError:
            print("Essa resposta é inválida, tente novamente")


def solicita_imc(peso,altura):
    resultado_imc = peso / (altura * altura)
    return resultado_imc

def solicita_classificao(resultado_imc):
    if resultado_imc < 18.5:
        print("Seu índice de massa corporal é:", resultado_imc)
        print("Sua classificação é: magreza.")
    elif resultado_imc >= 18.5 and resultado_imc < 24.9:
        print("Seu índice de massa corporal é:", resultado_imc)
        print("Sua classificação é: normal.")
    elif resultado_imc >= 25 and resultado_imc < 29.9:
        print("Seu índice de massa corporal é:", resultado_imc)
        print("Sua classificação é: sobrepeso.")
    elif resultado_imc >= 30 and resultado_imc < 34.9:
        print("Seu índice de massa corporal é:", resultado_imc)
        print("Sua classificação é: obesidade grau 1")
    elif resultado_imc >= 35 and resultado_imc < 39.9:
        print("Seu índice de massa corporal é:", resultado_imc)
        print("Sua classificação é: obesidade grau 2")
    elif resultado_imc >= 40:
        print("Seu índice de massa corporal é:", resultado_imc)
        print("Sua classificação é: obesidade grau 3")


altura_resultado = solicita_altura()
peso_resultado = solicita_peso()

solicita_classificao(solicita_imc(peso_resultado,altura_resultado))
