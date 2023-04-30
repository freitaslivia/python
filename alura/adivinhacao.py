import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) 
    total_tentativas = 0
    pontos = 1000

    print("Qhal o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível\n>"))
    # while (rodada <= total_tentativas):
    #     print("Tentativa {} de {}".format(rodada, total_tentativas))
    #     chute = int(input("Digite o seu número: "))
    #     print("voce digitou" , chute)

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format (rodada, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100\n>"))
        print("voce digitou" , chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um npumero entre 1 e 100! ")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else: 
            if(maior):
                print ("O seu chute foi maior do que o número secreto")
            elif(menor):
                print ("O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()