print("*Mensagem informativa")
jogo = True

while jogo:
    while True:
        print("mensagem inicial")

        escolha = input("O que voce quer fazer")

        if escolha in ["n", "nao"]:
            print("mensagem de final ruim 1")
            jogo = False
            break
        elif escolha in ["s", "sim"]:
            print("mensagem de progresso")
            break
        else:
            print("comando inválido. tente novamente")

    if not jogo:
        break

    while True:
        print("mensagem átrio")

        escolha = input("o que deseja fazer")

        if escolha in ["direita"]:
            print("mensagem de final ruim 2")
            jogo = False
            break
        if escolha in ["esquerda"]:
            print("mensagem de progresso 2")
            break
        else:
            print("Comando inválido. tente novamente")
    if not jogo:
        break

    while True:
        print("mensagem celas")

        escolha = input("o que quer fazer blablabla")

        if escolha in ["mesa"]:
            print("final ruim 3")
            jogo = False
            break

        if escolha in ["esqueleto"]:
            print("mensagem de progresso 3")
            break

        else:
            print("Comando inválido. tente novamente")

    if not jogo:
        break
    while True:
        print("mensagem esqueleto")

        escolha = input("O que deseja fazer")

        if escolha in ["roubar"]:
            print("mensagem final ruim 4")
            break
        elif escolha in ["bater"]:
            print("mensagem final bom")
            break
        elif escolha in ["correr"]:
            print("mensagem final de fuga")
            break
        else:
            print("Comando inválido. tente novamente")
    
    break

print("FIM DE JOGO")