def menu(opcao_menu):
  print("Agenda de Contatos")
  print("(C) - Cadastrar")
  print("(L) - Listar")
  print("(P) - Procurar")
  print("(S) - Sair")
  opcao_menu = input("Digite sua opção").upper()[0]


def entrar_dados():
  nome = input("Digite seu nome: ")
  tel = input("Digite seu telefone: ")
  email = input("Digite seu email: ")
  nascimento = input("Digite sua data de nascimento: ")
  obj = {"nome": nome, "email": email, "telefone": tel, "nascimento": nascimento}
  return obj


def procurar_dados():
  print("Contato encontrado:")
  print(f"Nome:      {cont['nome']:<40}")
  print(f"Telefone:  {cont['telefone']:<40}")
  print(f"eMail:     {cont['email']:<40}")
  print("Informe o que você deseja fazer com este contato: ")
  print("(A) - Apagar")
  print("(E) - Editar")
  print("(V) - Voltar ao menu principal")


lista = [
  {"nome": "João Silva", "telefone": "(11) 1234-5678", "email": "joao@teste.com"},
  {"nome": "Maria Silva", "telefone": "(11) 3434-1212", "email": "maria@teste.com"},
  {"nome": "Fabricio Orlando", "telefone": "(11) 4545-6767", "email": "fabricio@teste.com"},
  {"nome": "Maria Silva", "telefone": "(11) 3434-1212", "email": "maria2@teste.com"},
]

while True:
  opcao = menu()

  if opcao == 'C':
    contato = entrar_dados()
    lista.append(contato)
  elif opcao == 'P':
    nome_procurar = input("Qual nome você deseja procurar na lista: ")
    i = 0
    for cont in lista:
      if cont["nome"] == nome_procurar:
        procurar = procurar_dados()
        opcao_contato = input("Escolha sua opção:").upper()[0]
        if opcao_contato == 'A':
          lista.remove(cont)
          print("Contato apagado com sucesso")
        elif opcao_contato == 'E':
          print("Por favor digite novas informações para este contato:")
          lista[i] = entrar_dados()
          print("Informações alteradas com sucesso")
        elif opcao_contato == 'V':
          print("Retornando ao menu principal")
          break
      i = i + 1
  elif opcao == 'L':
    print("{:<40}{:^10}{:>30}".format("Nome", "Telefone", "Email"))
    for contato in lista:
      print("{:<40}{:^10}{:>30}".format(contato["nome"], 
      contato["telefone"], contato["email"]))
      print("\n\n\n")
  elif opcao == 'S':
    break