import random
import tkinter as tela

janela = tela.Tk()
janela.title("Jogo do cofre")
janela.geometry("600x500")

label = tela.Label(janela, text="Tente advinhar a senha secreta", font=("Arial", 16))
label.pack(pady=20)

entrada = tela.Entry(janela, width= 30)
entrada.pack(pady=10)


def menu():
    while True:
        opcao = entrada.get("Deseja jogar? [S/N] ").upper()
        
        if opcao == "S":
            jogar()
        elif opcao == "N":
            print("Que pena, Adeus")
            break
        else:
            print("Opção inválida")

def pedir_dificuldade():
    while True:
        try:
            dificuldade = int(input("Selecione o número de tentativas: "))
            return dificuldade
        except ValueError:
            print("Digite um número válido")


def jogar():
    senha = random.randint(1, 100)
    dificuldade = pedir_dificuldade()
    tentativas = 0



    while tentativas < dificuldade:


        try:
            chute = int(input("Qual número de 1 a 100? "))
            tentativas += 1
            if chute == senha:
                print("Parabéns, você acertou! ")
                return
            elif chute > senha:
                print("O número segredo é menor")
            else:
                print("O número segredo é maior")
            restantes = dificuldade - tentativas
            palavra = "tentativa" if restantes == 1 else "tentativas"
            print(f"Faltam {restantes} {palavra}")


        except ValueError:
            print("Por favor, tente novamente agora com um número")
            print("Toda vez que colocar um valor inváldio será descontado uma tentativa")
            print(f"Você tem {restantes} {palavra}")
            continue


    else: 
        print("Vocẽ perdeu, se quiser pode tentar novamente")
        print(f"O número era {senha}")
            
menu()





janela.mainloop()
