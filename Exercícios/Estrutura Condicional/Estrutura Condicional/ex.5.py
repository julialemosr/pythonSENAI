#Solicite ao usuário um número de 1 a 7 e exiba o nome correspondente ao dia da semana.
print("digite um número de 1 a 7 para descobrir o nome correspondente ao dia")
print("")
while True:
    try:
        dias = int(input("Digite um número de 1 a 7: "))
        if dias >= 1 and dias <= 7:
            break
        else:
            print("Esse número é inválido")

    except ValueError:
        print("Essa resposta é inválida, digite apenas números de 1 a 7")

if dias == 1:
    print("O número 1 é equivalente a domingo.")
elif dias == 2:
    print("O número 2 é equivalente a domingo.")
elif dias == 3:
    print("O número 3 é equivalente a domingo.")
elif dias == 4:
    print("O número 4 é equivalente a domingo.")
elif dias == 5:
    print("O número 5 é equivalente a domingo.")
elif dias == 6:
    print("O número 6 é equivalente a domingo.")
elif dias == 7:
    print("O número 7 é equivalente a domingo.")