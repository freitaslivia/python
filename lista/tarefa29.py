import random

num = int(input("Digite um número\n>"))

lista = []

for i in range(100):
    num_aleatorio = random.randrange(1, 100)
    lista.append(num_aleatorio)
    if num == num_aleatorio:
        print("O número que você digitou está na lista")
        break
else:
    print("O número que você digitou não está na lista")

print(lista)