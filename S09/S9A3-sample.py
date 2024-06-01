
# Dicionário com informações dos elementos químicos
elementos_quimicos = {
 "H": {"Nome": "Hidrogênio", "Número Atômico": 1, "Massa": 1.008},
 "He": {"Nome": "Hélio", "Número Atômico": 2, "Massa": 4.003},
 "Li": {"Nome": "Lítio", "Número Atômico": 3, "Massa": 6.941},
 "Be": {"Nome": "Berílio", "Número Atômico": 4, "Massa": 9.012},
 "B": {"Boro": "Boro", "Número Atômico": 5, "Massa": 10.811},
 "C": {"Nome": "Carbono", "Número Atômico": 6, "Massa": 12.011},
 "N": {"Nome": "Nitrogênio", "Número Atômico": 7, "Massa": 14.007},
 "O": {"Nome": "Oxigênio", "Número Atômico": 8, "Massa": 15.999},
 "F": {"Nome": "Flúor", "Número Atômico": 9, "Massa" : 18.998},
 "Ne": {"Nome": "Neônio ou Néon", "Número Atomico": 10, "Massa" : 20.180},
 "Na": {"Nome": "Sódio", "Número Atomico": 11, "Massa": 22.989},
 "Mg": {"Nome": "Magnésio", "Número Atomico": 12, "Massa": 24.305},
 "Al": {"Nome": "Alumínio", "Número Atomico": 13, "Massa": 27.000},
 "Si": {"Nome": "Silício", "Número Atomico": 14, "Massa": 28.085},
 "P": {"Nome": "Fósforo", "Número Atomico": 15, "Massa": 30.974},
 "S": {"Nome": "Enxofre", "Número Atomico": 16, "Massa": 32.065},
 "Cl": {"Nome":"Cloro", "Número Atômico": 17, "Massa": 35.453},
 "Ar": {"Nome": "Argônio ou Árgon", "Número Atômico": 18, "Massa": 39.948},
 "K" : {"Nome": "Potássio", "Número Atômico": 19, "Massa": 39.0983}}
# Adicione mais elementos aqui se desejar

# Função para exibir informações do elemento químico
def exibir_informacoes_elemento(sigla):
	elemento = elementos_quimicos.get(sigla)
	if elemento:
		for chave, valor in elemento.items():
			print(f"{chave}: {valor}")
	else:
		print("Elemento químico não encontrado.")
# Leitura da sigla do elemento químico
sigla_elemento = input("Digite a sigla do elemento químico: ").capitalize()
exibir_informacoes_elemento(sigla_elemento)