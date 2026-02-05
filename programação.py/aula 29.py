v = float(input("Qual é a velocidade atual do carro? "))
if v <= 80:
    print("Você não está acima do limite de velocidade")
    print("Tenha um bom dia")
    print("Dirija com cuidado!!!")
else:
    print("PARABENS SEU ANIMAL!!!!")
    print("Você está acima do limite de velocidade")
    print(f"Você foi multado em R${(v-80)*7}")
    print ("Por favor, faça o minimo e dirija com cuidado")

