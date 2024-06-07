def portaria_cine():
    age = int(input(f"Digite sua Idade: " ))
    if age >= 12 : # type: ignore
        print("Voce pode assistir o Filme, Divirta-se!!!")
    else:
        print("*** Sorry, but you can't watch this movie! access denied!!, Go Out! ***")

portaria_cine()
