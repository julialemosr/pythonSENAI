#Solicite dois números e verifica qual deles é o maior
print("digite 2 números para saber qual é o maior.")
print("")

while True:
    try:
        numero1 = float(input("digite o primeiro numero: "))
        break
    except ValueError:
        print("Não digite letras, apenas números")

while True:
    try:
        numero2 = float(input("digite o segundo numero: "))
        break
    except ValueError:
        print("Não digite letras, apenas números")


if numero1 > numero2:
    print("o número", numero1, "é maior que o", numero2)
else:
  print("o número", numero1, "é menor que o", numero2)