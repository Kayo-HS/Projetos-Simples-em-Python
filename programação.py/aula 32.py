from datetime import date
a = int(input("Digite um ano para analisar e 0 para analisar o ano atual:"))
if a == 0:
    a = date.today().year

ab = a / 4

if ab % 2 == 0:
    print(f"O ano {a} é bisexto")

else:
    print(f"O ano {a} não é bisexto")    
