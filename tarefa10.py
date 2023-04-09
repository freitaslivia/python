soma_das_cartas = int(input("Qual é a soma das cartas?"))


if soma_das_cartas <= 10:
    print("Sem dúvida compre mais uma carta")
elif soma_das_cartas >10 and soma_das_cartas<= 15:
    print("Há um risco, mas aconselho a comprar mais uma carta")
elif soma_das_cartas > 15 and  soma_das_cartas <= 20:
    print("Aconselho a parar de jogar")
elif soma_das_cartas == 21:
    print("Você já venceu, não precisa comprar mais nada")
elif soma_das_cartas > 21:
    print("Você perdeu")