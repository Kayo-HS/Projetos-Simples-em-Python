f = str(input("Digite uma frase: ")).strip()
fm = f.upper()
print(f"A letra 'A' aparece {fm.count("A")} vezes na frase.")
print(f"A primeira letra 'A' apareceu na posição {fm.find("A")+1}")
print(f"A última letra 'A' apareceu na posição {fm.rfind("A")+1}")
#.rfind começa a procurar da direita para esquerda ou seja do fim para o começo