salario = float(input("Digite seu salario:R$ "))
if salario <= 1250:
    p = salario * 0.15
    sf = p + salario
    print(f"PARABÉNS, seu novo salario é de R${sf:.2f}")
else:
    p1 = salario* 0.1
    s1 = p1 + salario
    print(f"PARABÉNS, seu novo salario é de R${s1:.2f}")

      
