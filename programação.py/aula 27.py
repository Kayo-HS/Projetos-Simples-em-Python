import random
import time


print("-=-"*30)
print("Vou pensar em um número entre 0 e 5. tente adivinhar...")
print("-=-"*30)

n = int(input("Em que número eu pensei? "))
print("Processando...")
time.sleep(4)

nums = [0,1,2,3,4,5]
np = random.choice(nums)
if n == (np):
    print("você acertou, parabens")
else:
    print(f"Eu pensei no número {np}, não no número {n}")    

