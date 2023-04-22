# índices   0  1    2  3   4   5   6    7  8     9   10, 11
numeros = [34, 67, 12, 9, 52, 13, 126, 42, 1, -128, -54, 87]

#a)
soma = 0
for n in numeros:
    soma += n
print("Soma de todos os elementos: ", soma)

#b)
produto = 1
for n in numeros:
    produto *= n
print("O produto de todos os elementos: ", produto)

#e)
maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print("O maior número: ", maior)

#f)
maior = max(numeros)
segundo_maior = numeros[0]
for n in numeros:
    if n > segundo_maior and n < maior:
        segundo_maior = n
print("O segundo maior número: ", segundo_maior)

#g)
menor = numeros[0]
for n in numeros:
    if n < menor:
        menor = n
print("O menor número: ", menor)

# h)
menor = min(numeros)
segundo_menor = numeros[0]
for n in numeros:
    if n > menor and n < segundo_menor:
        segundo_menor = n
print("O segundo menor número: ", segundo_menor)