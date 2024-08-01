# crie uma função que receba dois números como parâmetros.
# exiba o resultado das operações básicas de adição, subtração, multiplicação e divisão.
# 3.1 - Crie uma função que receba dois números como parâmetros para cada uma das operações básicas citadas acima retornando somente o valor das operações.
# 3.2 - Crie uma função que faça um menu para o usuário escolher a opção desejada.
#Descobrir oq quer fazer.

print("Insira dois números, escolha qual operação irá querer realizar e assim terá o resultado ")
print("")
def menu_calculadora():
    print("Menu calculadora")
    print("")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Realizar todas as contas")


def escolha_operacao():
    while True:
        try:
            escolha = int(input("Digite um número de 1 a 5: "))
            if escolha >= 1 and escolha <= 5:
                return escolha
            else:
                print("Digite apenas numeros entre 1 e 5")
        except ValueError:
            print("Essa resposta é inválida, digite apenas números de 1 a 5")


def solicitar_numero():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            return numero1,numero2
        except ValueError:
            print("Essa resposta é inválida, digite apenas números.")


def conta_adicao(numero1,numero2):
    adicao = numero1 + numero2
    return adicao


def conta_subtracao(numero1,numero2):
    subtracao = numero1 - numero2
    return subtracao


def conta_multiplicacao(numero1,numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao


def conta_divisao(numero1,numero2):
    divisao = numero1 / numero2
    return divisao


def exibir_resultados(escolha,numero1,numero2):
    if escolha == 1:
        print(f"A soma dos {numero1} + {numero2} é igual a{conta_adicao(numero1, numero2)}")

    elif escolha == 2:
        print(f"A subtração dos {numero1} - {numero2} é igual a {conta_subtracao(numero1,numero2)}")

    elif escolha == 3:
        print(f"A multplicação dos {numero1} * {numero2} é igual a {conta_multiplicacao(numero1,numero2)}")

    elif escolha == 4:
        print(f"A divisão dos {numero1} / {numero2} é igual a {conta_divisao(numero1,numero2)}")

    else:
        print(f"A soma dos {numero1} + {numero2} é igual a{conta_adicao(numero1, numero2)}")
        print(f"A subtração dos {numero1} - {numero2} é igual a {conta_subtracao(numero1, numero2)}")
        print(f"A multplicação dos {numero1} * {numero2} é igual a {conta_multiplicacao(numero1, numero2)}")
        print(f"A divisão dos {numero1} / {numero2} é igual a {conta_divisao(numero1, numero2)}")


menu_calculadora()
print("")
numero_calculadora = escolha_operacao()
n1, n2 = solicitar_numero()

exibir_resultados(numero_calculadora,n1,n2)