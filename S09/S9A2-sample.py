#Semana 9 Aula 2 : Arquivo Professor

#Mini Urna eletronica
#candidatos - id 1
candidato1_numero = 1
candidato1_partido = "Orion"
candidato1_nome = "João Cabral"
candidato1_vice = "Takuma Preça"

#candidatos - id 2
candidato2_numero = 2
candidato2_partido = "Scorpion"
candidato2_nome = "Neusa Sá"
candidato2_vice = "Mc Rosinha"

#Coletando entrada
numero_candidato = int(input("Digite o numero do candidato [1 ou 2]: "))

# Verificar as informações do candidato e exibir os dados
if numero_candidato == candidato1_numero:
    print("Candidato:", candidato1_nome)
    print("Partido:", candidato1_partido)
    print("Vice-prefeito:", candidato1_vice)
elif numero_candidato == candidato2_numero:
    print("Candidato:", candidato2_nome)
    print("Partido:", candidato2_partido)
    print("Vice-prefeito:", candidato2_vice)
else:
    print("Candidato não encontrado.")
   
print("___________________________________FIM____")