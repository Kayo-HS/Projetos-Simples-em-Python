n = str(input("Digite seu nome:")).upper().strip()
ns = n.split()
print(f"Seu primeiro nome é {ns[0]}")
print(f"Seu ultimo nome é {ns[-1]}")
# -1 serve para iniciar a leitura da direita para esquerda