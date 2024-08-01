from datetime import datetime

#crie uma função que receba um nome como parâmetro e escreva uma saudação baseada na hora atual
print("Você deverá digitar seu nome para receber uma saudação de acordo com o horário, Ex: Bom dia julia!!")
print("")
def solicita_nome(nome):
    while True:
        try:
            nome = input("Digite seu nome: ")
            if nome.isnumeric():
                print("Digite apenas letras")
            else:
                return nome
        except ValueError:
            print("Resposta invalida, digite apenas palavras.")

def define_saudacao(hora_atual):
    hora_atual == datetime.now().hour

    if hora_atual >= 0 and hora_atual <= 5:
        saudacao = "Boa madrugada"

    elif hora_atual > 5 and hora_atual <= 12:
        saudacao = "Bom dia"

    elif hora_atual > 12 and hora_atual <= 19:
        saudacao = "Boa tarde"

    else:
        saudacao = "Boa noite"

    return saudacao

#exibir saudacao e o nome.
print(define_saudacao(datetime.now().hour), solicita_nome(""),"!!")