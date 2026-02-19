import random

while True:
    opcao = input("Deseja jogar? [S/N] ")
    opcao_certa = opcao.upper()


    if opcao_certa == "S":
        try:
            dificuldade = int(input("Selecione o número de tentativas, quanto menor o número de tentaivas maior a dificulade: "))
            senha_escolhida_computador = random.randint(1,100)
            num_tentativas = 0
        except ValueError:
            print("Por favor, tente novamente agora com um número")
            continue


        while num_tentativas < dificuldade:


            try:
                num_tentativas += 1
                tentativas_restantes = dificuldade - num_tentativas 
                tentativas = "tentativa" if tentativas_restantes == 1 else "tentativas"
                num_escolhido_jogador = int(input("Qual número de 1 há 100 é a senha? "))
            
                if num_escolhido_jogador == senha_escolhida_computador:
                    print("Parabéns, Você acertou o número")
                    break
                elif num_escolhido_jogador > senha_escolhida_computador:
                    print("O número segredo é menor")
                    print(f"Faltam {tentativas_restantes} {tentativas}")
                
                elif num_escolhido_jogador < senha_escolhida_computador:
                    print("O número segredo é maior")
                    print(f"Faltam {tentativas_restantes} {tentativas}")
                
            except ValueError:
                print("Por favor, tente novamente agora com um número")
                print("Toda vez que colocar um valor inváldio será descontado uma tentativa")
                print(f"Você tem {tentativas_restantes} {tentativas}")
                continue


        else: 
            print("Vocẽ perdeu, se quiser pode tentar novamente")
            print(f"O número era {senha_escolhida_computador}")
            
    
    elif opcao_certa == "N":
        print("Que pena, Adeus")
        break
    else:
        print("Opção inválida")