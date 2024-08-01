#Solicite ao usuário um número de 1 a 12 e exiba o nome correspondente ao mês.
print("Digite um número de 1 a 12 para descobrir o mês correspodente.")
print("")

while True:
    try:
        mes = int(input("Digite um número de 1 a 12:"))
        if mes >= 1 and mes <= 12:
            break
        else:
            print("número inválido, Tente novamente.")

    except ValueError:
        print("Digite apenas número entre 1 e 12")

if mes == 1:
    print("O número é equivalente a janeiro.")
if mes == 2:
    print("O número é equivalente a fevereiro.")
if mes == 3:
    print("O número é equivalente a março.")
if mes == 4:
    print("O número é equivalente a abril.")
if mes == 5:
    print("O número é equivalente a maio.")
if mes == 6:
    print("O número é equivalente a junho.")
if mes == 7:
    print("O número é equivalente a julho.")
if mes == 8:
    print("O número é equivalente a agosto.")
if mes == 9:
    print("O número é equivalente a setembro.")
if mes == 10:
    print("O número é equivalente a outubro.")
if mes == 11:
    print("O número é equivalente a novembro.")
if mes == 12:
    print("O número é equivalente a dezembro.")