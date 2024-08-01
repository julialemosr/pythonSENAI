import random

numero_aleatorio = random.randint(1, 5)

print("Seja bem vindo ao jogo par ou impar!!! ")
print("Vamos as intruções: ")
print("")
print("1° O jogador deve escolher se vai ser par ou impar.")
print("2° O jogador deve escolher um número de 1 a 5.")
print("3° O jogo irá somar os números escolhidos.")
print("4° O jogo mostrará o ganhador e se a soma deu impar ou par.")
print("")
sair = 0
while True:
    try:
        comecar = int(input("Digite 0 para sair e 1 para jogar:"))

        if comecar == 0 or comecar == 1:
            break
        else:
            print("Digite somente os números 0 ou 1.")

    except ValueError:
        print("Digite apenas um número de 0 a 1.")

while comecar != sair:
    while True:
        try:
            par_impar = int(input(" digite 1 para par ou 2 para impar: "))
            if par_impar == 1 or par_impar == 2:

                escolha_numero = int(input("escolha o número de 1 a 5 que deseja jogar:"))

                if 0 < escolha_numero < 6:
                    print("o número escolhido por mim foi:", numero_aleatorio)
                    break

                else:
                    print("Digite somente um número entre 1 e 5")
            else:
                print("Digite somente o número 1 ou 2")
        except ValueError:
            print("Digite apenas números")

    print("")
    while comecar != sair:
        soma = numero_aleatorio + escolha_numero

        if soma % 2 == 0:
            # print("par")
            if par_impar == 1:
                print(soma, "é par, você ganhou.")
            else:
                print(soma, "é par, você perdeu.")

        else:
            # print("impar")
            if par_impar == 2:
                print(soma, "é impar, você ganhou.")
            else:
                print(soma, "é impar, você perdeu.")
        break

    comecar = int(input("Digite 0 para sair e 1 para jogar:"))

print("Fim de jogo.")
