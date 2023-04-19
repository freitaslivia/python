lista = [7, 4, 20, 35, 51, 42]

tamanho = len(lista)
print("Tamanho da lista: ", tamanho)

# i = 0
# while i < 6:
#     print(lista[i])
#    i = i + 1

# for i in range(0,6):
#     print(lista[])

# maior_numero = lista[0]
# for numero in lista:
#     if numero > maior_numero:
#         maior_numero = numero
# print("Maior número é: ", maior_numero)

menor_numero = lista[0]
for numero in lista:
    if numero < menor_numero:
        menor_numero = numero
print("Menor número é: ", menor_numero)