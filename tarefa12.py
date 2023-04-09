a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b
elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a
else:
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a

print(menor, meio, maior)