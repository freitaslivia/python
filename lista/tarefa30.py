import random

num = int(input("Digite um número\n>"))

lista = []

for i in range(100):
    num_aleatorio = random.randrange(1, 100)
    lista.append(num_aleatorio)
    if num == num_aleatorio:
        print("O número que você digitou está na lista")
        print(lista)
        break

ocorrencia = lista.count(num)
if ocorrencia > 0:
    print(f"O numero {num} aparece {ocorrencia} vezes" )
else:
    print("O número que você digitou não está na lista")



print(lista)