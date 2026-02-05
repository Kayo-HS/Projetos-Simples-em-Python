from datetime import date
HM = str(input("Digite seu genero com H ou M: ")). upper()
if HM == "M":
    print("Você é mulher e não presica servir ao exercito")
else:
    atual = date.today().year
    nasc = int(input("Digite seu ano de nascimento: "))
    idade = atual - nasc 
    print (f"Quem nasceu em {nasc} tem {idade} anos em {atual}")
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Você ainda não tem 18 anos. Aindam faltam {saldo} anos para o alistamento")
        ano = atual + saldo
        print(f"Seu alistamento será em {ano}")
    elif idade > 18:
        saldo = idade - 18
        print(f"Você já deveria ter se alistado há {saldo} anos.")
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}')
