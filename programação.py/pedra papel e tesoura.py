from random import randint

item = ("Pedra", "Papel", "Tesoura")

computador = randint(0, 2)

print("ESCOLHA COM SABEDORIA")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogador = int(input("Qual a sua jogada? "))
print("-=-"*10)
print(f"Jogador escolheu {item[jogador]}")
print(f"O computador escolheu {item[computador]}")
print("-=-"*10)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("Jogador GANHOU")
        print("Computador PERDEU")
    elif jogador == 2:
        print("Jogador PERDEU")
        print("Computador GANHOU")
    else:
        print("AÇÃO INVALIDA TENTE NOVAMENTE")

elif computador == 1:
    if jogador == 0:
        print("Jogador PERDEU")
        print("Computador GANHOU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("Jogador GANHOU")
        print("Computador PERDEU")
    else:
        print("AÇÃO INVALIDA TENTE NOVAMENTE")
elif computador == 2:
    if jogador == 0:
        print("Jogador GANHOU")   
        print("Computador PERDEU") 
    elif jogador == 1:
        print("Jogador PERDEU")
        print("Computador GANHOU")
    elif jogador == 2:
        print("EMPATE")
