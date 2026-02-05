valor_da_casa = float(input("Qual o valor da casa: R$ "))
salario = float(input("Digite seu salario atual: R$ "))
anos = int(input("Quantos anos de finaciamento: "))

anos_em_meses = anos * 12
parcela = valor_da_casa / anos_em_meses
minimo = salario * 0.3

print(f"Para comprar uma casa de {valor_da_casa:.2f} parcela seria {parcela:.2f}")

if parcela <= minimo:
    print("O emprestimo foi \033[1;32;44m APROVADO \033[m !!")
else:
    print("Lamento o emprestimo foi \033[1;33;41m negado \033[m")    








