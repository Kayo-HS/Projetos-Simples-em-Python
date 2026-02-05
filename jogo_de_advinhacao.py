import random



num_escolhido_computador = random.randint(1,100)
num_jogador = int(input("Qual número você escolhe? "))

while num_jogador != num_escolhido_computador:
        print("Você errou!!!")
        num_jogador = int(input("Qual número você escolhe? "))
        if num_jogador <= num_escolhido_computador:
            print("O número segredo é maior")
        elif num_jogador > num_escolhido_computador:
            print("O número segredo é menor") 
        else:
            print("VOCÊ GANHOU!!!!")
            break




