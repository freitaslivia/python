alunos = [{"nome": "livia", "nota": 7.0, "email": "livia@fiap.com"}, 
		 {"nome": "Louise", "nota": 10.0, "email": "louise@fiap.com"},
		 {"nome": "maria", "nota": 7.5, "email": "maria@fiap.com"}]

"""soma = alunos[0]["nota"] + alunos[1]["nota"] + alunos[2]["nota"]
media = soma/3.0
print("Soma: ", soma)
print("Media: ", media)
"""

soma = 0

"""Para vc deletar um elemento da lista: del alunos[0]
ou
a = alunos[2]
alunos.remove[m]
ou
m = alunos.pop(2)
"""

for aluno in alunos:
	soma = soma + aluno["nota"]

print("Soma: ", soma)
#print("Media", media)