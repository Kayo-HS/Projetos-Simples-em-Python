lista_de_numeros = []

while True:
    opcao = input("""Adicione numeros a lista: [S/N]
    [MAIOR] para mostrar o maior número, [MENOR] para mostrar o menor número
    [LER] para saber quantos números tem na sua lista
    [SAIR] para sair: """)


    opcao_certa = opcao.upper()
    if opcao_certa == "S":
        try:
            verificar_num = (float(input("Digite o número: ")))
        except ValueError:
            print("Entrada inválida! Tente um número")
        else:
            lista_de_numeros.append(verificar_num)
    elif opcao_certa == "N":
        print("Sua lista de núemros é:")
        for x in lista_de_numeros:
            print(x)
    elif opcao_certa == "MAIOR":
        if lista_de_numeros:
            print(f"O maior número é {max(lista_de_numeros)}")
        else:
            print("A lista está vazia.")
    elif opcao_certa == "MENOR":
        if lista_de_numeros:
            print(f"O menor número é {min(lista_de_numeros)}")
        else:
            print("A lista está vazia")
    elif opcao_certa == "LER":
        print(f"Tem {len(lista_de_numeros)} na sua lista de números")
    elif opcao_certa == "SAIR":
        break
    else:
        print("Opção inválida")
