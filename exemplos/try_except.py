# 0 while repete tudo que esta dentro dele
while True:
    # O try vai tentar executar esse bloco de codigos
    try:
        idade = int(input('Digite sua idade: '))

        # O if verifica se idade é válida
        if 0 < idade <= 100:
            print("idade", idade)
            # O break sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        # caso der erro executa aqui
        print("Digite sua idade em número, Ex: 26")
