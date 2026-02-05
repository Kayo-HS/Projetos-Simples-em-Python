multiplo_tabuada = int(input("Digite um número: "))
numero_comeco = int(input("Digite o número que a tabuada vai começar: "))
numero_final = int(input("Digite o número que a tabuada vai terminar: "))
numero_salto = int(input("Digite o número de saltos entre números: "))


if multiplo_tabuada <= 0 or numero_comeco <= 0 or numero_salto <= 0:
    print("Número deve ser maior que zero e inteiro")
else:
    for i in range(numero_comeco, numero_final+1, numero_salto):
        resultado = multiplo_tabuada * i
        print(f"{multiplo_tabuada} X {i} = {resultado}")
