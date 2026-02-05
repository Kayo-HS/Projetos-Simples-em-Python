nome = str(input("Qual seu nome? ")).upper().strip()
if nome == "KAYO":
    print ("Que nome lindo você tem!!!")
elif nome == "JOÃO" or nome == "MARIA" or nome == "ENZO":
    print("Que nome generico você tem em")
elif nome in "ISABELA":
    print("O nome do amor da minha vida em")
else:
    print("Seu nome é bem feio em")
print(f"Tenha um otimo dia, {nome}!! ")
