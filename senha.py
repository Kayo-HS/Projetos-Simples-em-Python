import hashlib
import time
import os

# ===== CONFIGURAÇÕES =====
senha_real = input("Defina uma senha numérica (ex: 1234): ")
tamanho = len(senha_real)

# Gera o hash da senha (simulando um banco de dados)
hash_senha = hashlib.sha256(senha_real.encode()).hexdigest()

os.system("clear")
print("Hash armazenado no sistema:")
print(hash_senha)
print("\nIniciando ataque de brute force...\n")

# ===== BRUTE FORCE =====
tentativas = 0
inicio = time.time()

for i in range(10 ** tamanho):
    tentativa = str(i).zfill(tamanho)
    hash_tentativa = hashlib.sha256(tentativa.encode()).hexdigest()
    tentativas += 1

    if hash_tentativa == hash_senha:
        fim = time.time()
        print("\n✅ Senha encontrada!")
        print(f"Senha: {tentativa}")
        print(f"Tentativas: {tentativas}")
        print(f"Tempo gasto: {fim - inicio:.2f} segundos")
        break

    if tentativas % 1000 == 0:
        print(f"Tentativas: {tentativas} | Atual: {tentativa}", end="\r")
