print("-=-"*20)
print("Analisador de Triângulos")
print("-=-"*20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("Os segmentos acima podem formar triângulo!!!")
    if r1 == r2 == r3:
        print("Seu triângulo é Equilátero, todos os lados são iguais")
    elif r1 != r2 != r3 != r1:
        print("Seu triângulo é Escaleno")
    else:
        print("Seu triângulo é Isóceles")
else: 
    print("Os segmentos não podem formar um triângulo")
    