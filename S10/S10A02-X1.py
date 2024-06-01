
#S10A02-Exercicio 1 - senha
while True:
    senha = input("Crie uma senha (deve ter pelo menos 8 caracteres e conter números e letras): ")
    if len(senha) >= 8 and any(char.isdigit() for char in senha) and any(char.isalpha() for char in senha):
        print("Senha criada com sucesso!")
        break
    else:
        print("A senha não atende aos critérios, tente novamente.")

