


tru = True

while tru:
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if nome != senha:
        print("logou no sistema!")
        break
    else:
        print("Senha e nome de usuário invalidos")
        continue
