lista = []
opcao = ''

while opcao != 'S':

    opcao = input("\n\t(C)adastrar\n\t(L)istar\n\t(P)rocurar\n\t(S)air\n\t>").upper()

    if opcao == 'C':
        marca = input("Digite a marca\n>")
        placa = input("Digite a placa\n>")
        ano = input("Digite o ano\n>")
        modelo = input("Digite o modelo\n>")

        informacao_carro = {"marca": marca, "placa": placa, "ano": ano, "modelo": modelo}
        lista.append(informacao_carro)

    elif opcao == 'L':
        for info in lista:
           print("Marca:\t", info["marca"], "\nPlaca:\t", info["placa"], "\nAno:\t", info["ano"], "\nModelo:\t", info["modelo"], "\n")
    elif opcao == 'P':
        procurar_placa = input("Qual é a placa do seu carro? ")
        encontrado = False
        for info in lista:
            if info["placa"] == procurar_placa:
                encontrado = True
                print("Marca:\t", info["marca"], "\nPlaca:\t", info["placa"], "\nAno:\t", info["ano"], "\nModelo:\t", info["modelo"], "\n")
                print("Qual das opicoes abaixo?")
                opcao2 = input("(A)lterar\n(E)xcluir\n(R)etornar ao menu principal\n>").upper()

                if opcao2 == 'A':
                    info["marca"] = input("Digite a marca\n>")
                    info["placa"] = input("Digite a placa\n>")
                    info["ano"] = input("Digite o ano\n>")
                    info["modelo"] = input("Digite o modelo\n>")
            elif opcao2 == 'R':
                break