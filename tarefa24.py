altura = int(input("Digite a altura do triângulo: "))
comprimento = int(input("Digite o comprimento do triângulo: "))

for i in range(altura):
    for j in range(min(i+1, comprimento)):
        print('*', end='')
    print()

for i in range(altura-1, 0, -1):
    for j in range(min(i, comprimento)):
        print('*', end='')
    print()
