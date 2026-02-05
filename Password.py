import os 
from random import randint

pas = input("Password only numbers: ")

keys = [1,2,3,4,5,6,7,8,9,0]

pwg = ""
while(pwg!= pas):
    pwg=""
    for i in range(len(pas)):
        guessPass = keys[randint(0,4)]
        pwg += str(guessPass)
        print(pwg)
        print("Adinhando a senha...por favor espere!")
        os.system("clear")

print(f"A senha é: {pwg}")
