#Solicite duas notas de um aluno e calcule a média.
print("digite suas 2 notas entre 0 a 100 para saber a média")
print("")

while True:
    try:
        nota1 = float(input("Nota 1: "))
        if nota1 >= 0 and nota1 <= 100:
            break
        else:
            print("Nota 1 invalida")

    except ValueError:
        print("Não digite letras, apenas números")

while True:
    try:
        nota2 = float(input("Nota 2: "))
        if nota2 >= 0 and nota2 <= 100:
            break
        else:
            print("Nota 2 invalida")

    except ValueError:
        print("Não digite letras, apenas números")

media = (nota1 + nota2) / 2

if 70 <= media <= 100:
    print(f"sua media é {media}, você foi aprovado")
elif 0 <= media <= 70:
    print(f"sua media é {media},você foi reprovado")