opcao = input("Digite S ou N \t \n>").upper()

while opcao != "S" and opcao != "N":
    print("Vc digitou {}, digite S ou N\t \n> ".format(opcao))
    opcao = input("Digite S ou N\t").upper()

print("Vc digitou {}".format(opcao))

