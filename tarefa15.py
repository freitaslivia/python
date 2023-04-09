numero = int(input("Digite um número: "))
maximo = int(input("Digite o multiplicador máximo: "))

print("Tabuada do", numero)
for i in range(1, maximo+1):
    resultado = numero * i
    print(numero, "X", i, "=", resultado)


