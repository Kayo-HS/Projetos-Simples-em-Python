kg = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(M) : "))

imc = kg / (altura **2) 

print(f"Seu IMC é {imc:.1f}")

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Você está no peso ideal")
elif imc < 30:
    print("Você está com sobrepeso")
elif imc < 40:
    print("Você tem obesidade")
else:
    print("Obesidade mórbida")