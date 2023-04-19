
# cp1 = float(input("Digte a nota do seu primeiro cp: "))
# cp2 = float(input("Digte a nota do seu segundo cp: "))
# cp3 = float(input("Digte a nota do seu terceiro cp: "))
# cp4 = float(input("Digte a nota do seu quarto cp: "))
# cp5 = float(input("Digte a nota do seu quinto cp: "))
# cp6 = float(input("Digte a nota do seu sexto cp: "))
# gs = float(input("Digte a nota do seu gs: "))
# cha1 = float(input("Digte a nota da primeira entrega do challenge: "))
# cha2 = float(input("Digte a nota da segunda entrega do challenge: "))

# print("Suas notas são: ")
# notas = [cp1, cp2, cp3, cp4, cp5, cp6, gs, cha1, cha2]
# print(notas)

print("Progama que cacula a média final")
notas = []

for i in range(6):
    cp = float(input("Digite a nota do CP #{}: ".format(i + 1)))
    notas.append(cp)

cha1 = float(input("Digte a nota da primeira entrega do challenge: "))
notas.append(cha1)

cha2 = float(input("Digte a nota da segunda entrega do challenge: "))
notas.append(cha2)

gs = float(input("Digte a nota do global solution: "))
notas.append(gs)

print("Notas: ")
print(notas)

soma = 0
for n in notas:
    soma = soma + n

media = soma / 9.0

print("Média: ", media)


