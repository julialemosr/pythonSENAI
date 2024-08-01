# Solicite ao usuário o valor de sua renda anual bruta, calcule e exiba o desconto.
print("Digite o valor de sua renda anual bruta.")
print("")

while True:
    try:
        renda = float(input("Digite o valor de sua renda anual bruta: R$"))
        break

    except ValueError:
        print("Essa resposta é invalida, digite apenas números")

if renda <= 56072.00:
    print("Você não tem desconto.")

elif renda > 56072.00 and renda <= 238532.00:
    desconto1 = (7.50 / 100) * renda
    print(f" Seu desconto é de R${desconto1}")

elif renda > 238532.00 and renda <= 522400.00:
    desconto2 = (15 / 100) * renda
    print(f"Seu desconto é de R${desconto2}")

elif renda > 522400.00 and renda <= 987600.00:
    desconto3 = (22.50 / 100) * renda
    print(f"Seu desconto é de R${desconto3}")

elif renda > 987600.00:
    desconto4 = (27.50 / 100) * renda
    print(f"Seu desconto é de R${desconto4}")