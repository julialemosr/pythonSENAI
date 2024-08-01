#Solicite ao usuário três números inteiros e mostre o maior deles.
print("Digite 3 números inteiros para saber qual é o maior deles.")
print("")

while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro:"))
        break

    except ValueError:
        print("Essa resposta é inválida, digite apensas números inteiros.")

while True:
    try:
        numero2 = int(input("Digite o segundo número inteiro:"))
        break

    except ValueError:
        print("Essa resposta é inválida, digite apensas números inteiros.")

while True:
    try:
        numero3 = int(input("Digite o terceiro número inteiros:"))
        break

    except ValueError:
        print("Essa resposta é inválida, digite apensas números inteiros.")

if numero1 == numero2 == numero3:
  print ("Ambos tem o mesmo valor ")
elif numero1 > numero2:
    if numero2 > numero3:
        print(f"o número {numero1} é o maior.")
    elif numero2 > numero3:
        print(f"o número {numero2} é o maior.")
else:
  print(f"o número {numero3} é o maior.")