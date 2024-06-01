# Exercício 2: Refatoração de Código com Laço while

# Os alunos devem identificar que o segundo break faz com que o laço encerre prematuramente, 
# impedindo a impressão dos números de 2 a 10. 
# Eles devem remover o break incorreto e garantir que o laço funcione conforme o esperado.

# abaixo o algoritmo proposto
# numero = 1
""" while True:
    print(numero)
    numero += 1
    if numero > 10:
        break
    break
 """



# abaixo uma solução bem refatorada
""" numero = 1
while numero <= 10:
    print(numero)
    numero += 1 """

for numero in range(1,11):
    print(numero)
