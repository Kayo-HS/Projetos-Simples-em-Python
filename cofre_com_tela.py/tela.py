import tkinter as tela

janela = tela.Tk()
janela.title("Jogo do cofre")
janela.geometry("600x500")

label = tela.Label(janela, text="Tente advinhar a senha secreta", font=("Arial", 16))
label.pack(pady=20)

janela.mainloop()