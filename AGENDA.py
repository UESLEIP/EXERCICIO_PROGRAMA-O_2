menu = '''------ Agenda ------
1- Add Contato
 2- Remover Contato
 3- Listar Contatos
 0- Sair
Opção: '''
lista_ids = []
lista_nomes = []
lista_telefones = []
cont_id = 1  # contador de IDs
while True:
    opcao = input(menu)
    if opcao == "1":
        if len(lista_ids) < 10:
            print("-- Adicionando --")
            lista_ids.append(str(cont_id))
            nome = input("Nome do contato: ")
            lista_nomes.append(nome)
            telefone = input(f"Telefone de {nome}: ")
            lista_telefones.append(telefone)
            print(f"{nome} foi adicionado à Agenda.")
            cont_id += 1
        else:
            print("Agenda cheia!")
    elif opcao == '2':
        print("-- Removendo --")
        id = input("Digite o ID do contato: ")
        if id in lista_ids:
            for posicao in range(len(lista_ids)):
                if id == lista_ids[posicao]:
                    print(f"{lista_nomes[posicao]} removido da agenda.")
                    lista_ids.pop(posicao)
                    lista_nomes.pop(posicao)
                    lista_telefones.pop(posicao)
                    break
        else:
            print(f" ID {id} não encontrado!")
    elif opcao == '3':
        print('-- Listagem --')
        if lista_ids != []:
            for posicao in range(len(lista_ids)):
                print(f'ID: {lista_ids[posicao]}  Nome: {lista_nomes[posicao]} Telefone: {lista_telefones[posicao]}')
        else:
            print("Agenda vazia!!!")
    elif opcao == "0":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")