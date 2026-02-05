d = int(input("Digite a distância:KM "))
if d >= 200:
    print(f"Com o valor promocional a passagem custa R${d*0.45:.2f}")
else: 
    print(f"O valor da passagem custa R${d*0.50:.2f}")
