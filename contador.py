contador = int(input("Digite o número do começo da contagem: "))
chegada_contador = int(input("Digite até quer que seja contado: "))
como_sera_contado = int(input("Digite como será contado: "))


while contador <= chegada_contador:
    print(contador)
    contador += como_sera_contado

