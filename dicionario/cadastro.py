#nome email e telefone
lista = []


while True:
    print("Agenda de contatos")
    print("(C) - Cadastrar")
    print("(L) - Listar")
    print("(S) - Sair")

    opcao = input("Digite sua opção\n>").upper()
    if opcao == 'C':
        nome = input("Digite seu nome\n>")
        telefone = input("Digite seu telefone\n>")
        email = input("Digite seu email\n>")
        contato = {"nome": nome, "email": email, "telefone": telefone}
        lista.append(contato)

    elif opcao == 'L':
        print("{:<40}{:^10}{:>30}".format("Nome", "Telefone", "Email"))

        for c in lista:
            print("{:<40}{:^10}{:>30}".format(c["nome"], c["telefone"], c["email"]))
            print("\n\n\n")

    elif opcao == 'S':
        break
   
