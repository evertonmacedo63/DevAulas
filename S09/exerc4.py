import random

def jogo_adivinha():
    secret_num = random.randint(1,100)
    tentativas = 0
    palpite = 0

    while palpite!= secret_num:
          palpite= int(input("Advinhe o número entre 1 e 100:"))
          tentativas += 1

          if palpite < secret_num:
              print(" Mais alto!")
          elif palpite > secret_num:
               print ("Mais baixo!")

    print(f"Parabéns! Você acertou o número secreto {secret_num} em {tentativas} tentativas.")              

jogo_adivinha()
