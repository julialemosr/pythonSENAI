#solicite ao usuario um número e verifique se é positivo ou negativo
print("digite um numero para descobrir se ele é positivo ou negativo")
print("")

while True:
    try:
        numero = (float(input("digite um número: ")))
        if numero < 0:
            print(f"o número {numero} é negativo")

        elif numero > 0:
            print(f"o número {numero} positivo")

        break

    except ValueError:
        print("Não digite letras, apenas números")