vitorias = int(input("Quantas vezes você ganhou? "))
derrotas = int(input("Quantas vezes você perdeu? "))

def calculadora (vitorias, derrotas):
    saldo = vitorias - derrotas
    return saldo 


saldo = calculadora(vitorias, derrotas)


if saldo <= 10:
    rank = "Ferro"

elif saldo >= 11 and saldo <= 20:
    rank = "Bronze"

elif saldo >= 21 and saldo <= 50:
    rank = "Prata"

elif saldo >= 51 and saldo <= 80:
    rank = "Ouro"

elif saldo >= 81 and saldo <= 90:
    rank = "Diamante"

elif saldo >= 91 and saldo <= 100:
    rank = "Lendário"

elif saldo >= 101:
    rank = "Imortal"

else:
    print ("Erro, Tente novamente")
      

print(f"O Herói tem de saldo {saldo} e está no nível de {rank}")
