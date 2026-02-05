from datetime import date
atual = date.today().year

nascimento = int(input("Ano de nascimento: "))

idade = atual - nascimento

if idade <= 9:
    print("Atleta Mirim")

elif idade > 10 and idade <= 14:
    print("Atleta Infantil")

elif idade > 14 and idade <= 19:
    print("Atleta Junior")

elif idade > 19 and idade <= 25:
    print("Atleta Sênior")
    
else:
    print("Master")