print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3


# while (rodada <= total_tentativas):
#     print("Tentativa {} de {}".format(rodada, total_tentativas))
#     chute = int(input("Digite o seu número: "))
#     print("voce digitou" , chute)

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
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