jogador1 = int(input("Jogador 1, informe quantos blocos empilhou: "))
jogador2 = int(input("Jogador 2, informe quantos blocos empilhou: "))
jogador3 = int(input("Jogador 3, informe quantos blocos empilhou: "))

if jogador1 > jogador2 and jogador1 > jogador3:
    print("Jogador 1 venceu com", jogador1, "blocos empilhados!")
elif jogador2 > jogador1 and jogador2 > jogador3:
    print("Jogador 2 venceu com", jogador2, "blocos empilhados!")
elif jogador3 > jogador1 and jogador3 > jogador2:
    print("Jogador 3 venceu com", jogador3, "blocos empilhados!")
else:
    print("Houve empate entre os jogadores!")