palavra_secreta = "misterio"
letras_acertadas = ['_' for _ in palavra_secreta]
erros = 0

while erros < 3 and '_' in letras_acertadas:
    palpite = input("Digite uma letra: ").lower()
    if palpite in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[i] = palpite
    else:
        erros += 1
        print(f"Erro! Você tem {3 - erros} tentativas restantes.")

    print(" ".join(letras_acertadas))

if '_' not in letras_acertadas:
    print("Parabéns, você adivinhou a palavra!")
else:
    print(f"Você perdeu. A palavra era: {palavra_secreta}.")
