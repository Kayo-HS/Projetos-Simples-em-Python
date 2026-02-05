compra = float(input("Digite o valor da sua compra R$: "))

print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

opção = int(input("Qual é a opção: "))

if opção == 1:
    desconto = compra * 0.1
    print(f"Sua compra de R${compra:.2f} com DESCONTO por ser avista fica por R${compra-desconto:.2f}")
elif opção == 2:
    desconto = compra * 0.05
    print(f"Sua compra de R${compra:.2f} com DESCONTO por ser avista no cartão fica por R${compra-desconto:.2f}")
elif opção == 3:
    divido = compra / 2
    print(f"Sua compra no total fica R${compra:.2f}, dividido em 2x as parcelas ficam em {divido:.2f} ")
elif opção == 4:
    parcelas = int(input("Quantas parcelas: "))
    juros = compra * 0.20
    divido = (compra + juros) / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de R${divido:.2f}")
    print(f"Sua compra de R${compra:.2f} vai custar R${compra + juros:.2f} no final")
else:
    print ("Opção INVALIDA, Tente novamente")
