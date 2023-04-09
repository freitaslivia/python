altura = int(input("Digite a altura do triângulo retângulo: "))
comprimento = int(input("Digite o comprimento do triângulo retângulo: "))

for i in range(altura):
    for j in range(min(i+1, comprimento)):
        print('*', end='')
    print()