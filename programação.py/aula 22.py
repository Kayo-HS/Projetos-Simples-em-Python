nome = str(input("Digite seu nome completo: ")).strip()
n1 = nome.split()
separa = nome.split()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculo: {nome.upper()}")
print(f"Seu nome em minúsculo: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)-nome.count(" ")} letras")
print(f"Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras")


 
