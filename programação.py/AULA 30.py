n = int(input("Digite um número:"))
if n % 2 == 0:
    print("par")
else:
    print("impar")    
# o "%" serve para dizer o seguinte: "se o numero por dividido por 2 e o resultado for igual a zero ele é par se não é impar"
# exemplo: 10/2 == 5.0 <---- o zero ta aqui entao 10 é par 
# 5/2 == 2.5 <----- não tem zero então é impar( para saber se o numero é impar ou par só dividir por 2 número inteiro == par, número quebrado == impar)