n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2)/2

if media <= 5.0:
    print("REPROVADO")
elif media >= 7.0:
    print("APROVADO, PARABÉNS")
else:
    print("Você está de recuperação")
# pode colocar para uma nota entre 5.0 e 6.9 o seguite codigo(if media >= 5 and media <7: )
