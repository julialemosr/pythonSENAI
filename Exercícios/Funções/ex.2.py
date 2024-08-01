# Crie uma função que receba um valor de temperatura em graus Celsius como parâmetro.
# retorne o valor convertido para Fahrenheit e Kelvin.

print("Você deverá digitar a temperatura em graus Celcius para descobrir este valor em graus Fahrenheit e Kelvin")
print("")
def receber_temperatura():
    while True:
        try:
            temperatura = int(input("Digite uma temperatura em graus Celsius:"))
            return temperatura
        except ValueError:
            print("Essa resposta é inválida, digite apenas números.")


def converter_temperatura1(temperatura):
    fahrenheit = temperatura * 1.8 + 32
    print("A temperatura em Fahrenheit é", fahrenheit)


def converter_temperatura2(temperatura):
    kelvin = temperatura + 273
    print("A temperatura em Kelvin é",kelvin )


#exibi a temperatura em Fahrenheit e Kelvin
temperatura_celsius = receber_temperatura()

converter_temperatura1(temperatura_celsius)
converter_temperatura2(temperatura_celsius)


