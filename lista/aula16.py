numeros = [34, 67, 12, 9, 52]
indice = 0 
indice_bloco = 0
temp = []

for num in numeros:
    num = numeros[indice]
    temp.append(num)
    indice_bloco = indice_bloco + 1

    if indice_bloco >= 2:
        temp = []
        indice_bloco = 0
indice + indice + 1
print(temp)        


