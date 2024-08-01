#Utiliza a biblioteca datetime para mostrar o ano, mes e dia da semana e pegar o horário atual e dar uma saudação para o usuário.

#datetime biblioteca de tempo/data
import datetime

#alimentar variavel com o tempo agora
tempo = datetime.datetime.now()
ano = tempo.year
mes = tempo.month
#semana = tempo.weekday()
semana = tempo.strftime("%w")
hora = tempo.hour
minuto = tempo.minute
segundo = tempo.second
dia = tempo.day
#semanas = 0

print(f'TESTE: {semana}')

if tempo.month == 1:
    meses ="Janeiro"

elif tempo.month == 2:
    meses = "Fevereiro"

elif tempo.month == 3:
    meses = "Março"

elif tempo.month == 4:
    meses = "Abril"

elif tempo.month == 5:
    meses = "Maio"

elif tempo.month == 6:
    meses = "Junho"

elif tempo.month == 7:
    meses = "Julho"

elif tempo.month == 8:
    meses = "Agosto"

elif tempo.month == 9:
    meses = "Setembro"

elif tempo.month == 10:
    meses = "Outubro"

elif tempo.month == 11:
    meses = "Novembro"

elif tempo.month == 12:
   meses = "Dezembro"


if semana == 0:
   semanas = "Domingo"

elif semana == 1:
    semanas = "Segunda-feira"

elif semana == 2:
    semanas = "Terça-feira"

elif semana == 3:
    semanas = "Quarta-feira"

elif semana == 4:
    semanas = "Quinta-feira"

elif semana == '5':
    semanas = "Sexta-feira"

elif semana == 6:
    semanas = "Sábado"


if hora < 12:
    saudacao = "Bom dia!!"

elif hora >= 12 and hora < 18:
    saudacao = "Boa tarde!!"
else:
    saudacao = "Boa noite!!"

print(f"{saudacao} hoje é {semanas}, dia {dia} de {meses} 7 de {ano} - Agora são {hora}:{minuto}:{segundo}")