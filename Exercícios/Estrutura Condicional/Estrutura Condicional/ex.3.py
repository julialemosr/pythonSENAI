#Solicite o ano de nascimento de uma pessoa, calcule a idade e verifique se a pessoa é maior ou menor de idade.
print("digite o ano que estamos e o ano que vc nasceu para saber se você é maior ou menor de idade")
print("")

while True:
    try:
        ano_atual = int(input("digite o ano em que estamos: "))
        if ano_atual == 2024:
            break
        else:
            print("essa resposta é inválida")

    except ValueError:
        print("Não digite letras, apenas números")

while True:
    try:
        nascimento = int(input("digite o seu ano de nascimento: "))
        if nascimento >= 1910 and nascimento <= 2024:
            break
        else:
            print("essa resposta é inválida")

    except ValueError:
        print("Não digite letras, apenas números")

idade = ano_atual - nascimento

if idade >= 18:
    print(f"Você tem {idade} anos, você é maior de idade.")
elif idade <= 17:
    print(f"Você tem {idade} anos,você é menor de idade.")