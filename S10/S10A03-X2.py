# Pode-se melhorar o controle do laço while?
# A variável encontrada é realmente necessária?
# Existe uma maneira mais eficiente de encontrar o primeiro número que atende à condição? "

# Inicia a partir de 1500 e incrementa de 5 em 5, pois estamos procurando um número divisível por 5. óbvio ululante!!!
# Isso reduz o número de iterações necessárias.
# inicio : int = 1773
# fim : int = 4800
# for numero in range(inicio, fim, 5):
for numero in range(1591, 2701, 5):
    if numero % 7 == 0:
       # print(f"O primeiro número divisível por 5 e 7 entre {inicio} e {fim}  é:  {numero}")
        print(f"O primeiro número divisível por 5 e 7 entre 1500 e 2700 é: {numero}")
        break
