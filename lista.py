lista_de_compra = []

while True:
    opcao = input("Deseja Adicionar itens a lista de compra? [S/N]:")
    opcao_certa = opcao.upper()
    if opcao_certa == "S":
        lista_de_compra.append(input("Adicione itens a lista de compras:"))
    elif opcao_certa == "N":
        print("Sua lista de compra para esse mês é:")
        for x in lista_de_compra:
            print(x)
        break
    else:
        print("Opção Inválida")
