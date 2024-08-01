# Crie uma função que receba três números como parâmetros que serão os lados de um triângulo
# retorne se ele é equilátero, isósceles ou escaleno.
# Equilátero se todos os lados possuem a mesma medida.
# Isósceles se dois lados possuem a mesma medida.
# Escaleno se todos os lados possuem medidas diferentes.

print("Digite os lados do triângulo que deseja calcular para saber se são equilátero, escaleno ou isósceles.")
print("")
def lados_triangulo():
    while True:
        try:
            lado1 = int(input("Digite o primeiro lado do triângulo: "))
            lado2 = int(input("Digite o segundo lado do triângulo: "))
            lado3 = int(input("Digite o terceiro lado do triângulo: "))
            return lado1, lado2, lado3
        except ValueError:
            print("Resposta inválida, digite apenas números")


def triangulos(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilatero")

    elif lado1 != lado2 and lado2 != lado3:
        print("Triângulo Escaleno")

    else:
        print("Triângulo Isósceles")


lado1, lado2, lado3 = lados_triangulo()
triangulos(lado1, lado2, lado3)
