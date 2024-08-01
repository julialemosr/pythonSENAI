import random

numero_aleatorio = random.randint(1, 100)

print("Bem vindo ao jogo de adivinhação de números!!")
print("Vamos as instruções:")
print("1° O jogo escolherá um número entre 1 e 100 aleatoriamente, sem que o jogador saiba.")
print("2° O jogador deverá fazer um chute de um número.")
print("3° O jogo irá mostrar se esse número é maior ou menor que o número escolhido.")
print("4° Isso irá se repetir até acertar o número sorteado")
print("")

while True:

    try:
        entrada = int(input("Digite 1 se você quer jogar e 0 se você quer sair: "))

        if entrada == 0 or entrada == 1:
            break
        else:
            print("Digite somente os números 0 ou 1.")

    except ValueError:
        print("Digite apenas um número de 0 a 1.")

while True:
    try:
        chute = int(input("Digite o número que deseja testar: "))

        if 0 <= chute <= 100:
            break
        else:
            print("Digite somente os números de 0 a 100.")

    except ValueError:
        print("Digite apenas números de 0 a 100.")

sair = 0
numero_aleatorio = random.randint(1, 100)

while entrada != sair:

    if chute > numero_aleatorio:
        print("O número testado é maior que o escolhido pelo jogo!")

    elif chute < numero_aleatorio:
        print("O número testado é menor que o escolhido pelo jogo!")

    elif chute == numero_aleatorio:
        print("Você acertou, parabéns!!")

        entrada = int(input("Digite 1 se você quer jogar e 0 se você quer sair: "))
        numero_aleatorio = random.randint(1, 100)

    while True:
        try:
            chute = int(input("Digite o número que deseja testar: "))

            if 0 <= chute <= 100:
                break
            else:
                print("Digite somente os números de 0 a 100.")

        except ValueError:
            print("Digite apenas números de 0 a 100.")


print("Fim do jogo!")