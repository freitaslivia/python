print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("voce digitou" , chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")
else: 
    if(maior):
        print ("O seu chute foi maior do que o número secreto")
    elif(menor):
        print ("O seu chute foi menor do que o número secreto")

print("Fim do jogo")