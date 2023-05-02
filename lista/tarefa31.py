
numeros = []

for i in range(7):
    num = int(input("Digite um número: "))
    numeros.append(num)

soma = 0
medias = []
for i in range(7):
    soma = soma + numeros[i]
    media = soma / (i + 1)
    medias.append(media)

print("Número\t Soma \t Média")
for i in range(7):
    print("{}\t{}\t{}".format(numeros[i], soma, medias[i]))