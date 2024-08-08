import os
def clear_screen():
    os.system('cls')

def resu_cli(nome, endereco, cpf):
    clear_screen()
    rece_cliente = []
    rece_cliente.append(nome)
    print("\nNOME REGISTRADO COM SUCESSO")

    
    rece_cliente.append(endereco)
    print("ENDEREÇO REGISTRADO COM SUCESSO")

    
    if len(cpf) == 14 or len(cpf) == 11:
        rece_cliente.append(cpf)  
        print("CPF REGISTRADO COM SUCESSO")    
    else:
        print("CPF INVALIDO!!")
        rece_cliente.append(" ")
    clientes.append(rece_cliente)
    rece_cliente = [] 
    input("\nContinue...")

def resu_funcio(nome, endereco, cpf):
    clear_screen()
    rece_funcionario = []
    rece_funcionario.append(nome)
    print("\nNOME REGISTRADO COM SUCESSO")

    
    rece_funcionario.append(endereco)
    print("ENDEREÇO REGISTRADO COM SUCESSO")

    
    if len(cpf) == 14 or len(cpf) == 11:
        rece_funcionario.append(cpf)  
        print("CPF REGISTRADO COM SUCESSO")    
    else:
        print("CPF INVALIDO!!")
        rece_funcionario.append(" ")
    funcionario.append(rece_funcionario)
    rece_funcionario = [] 
    input("Continue...")


funcionario = []


"""CLIENTE"""
dec = False
num = 0
clientes = []

while dec == False:
    clear_screen()
    res = input("\n1 - CADASTRAR CLIENTE\n2 - CADASTRAR FUNCIONARIO\n3 - VER LISTA DE CLIENTES CADASTRADOS\n4 - VER LISTA DE FUNCIONARIOS CADASTRADOS\n\nOpção: ").strip().upper()
    if res == "1":
        nome_fun = input("\nDigite o nome do cliente: ").capitalize().strip()
        resu_cli(nome_fun, endereco = input(f"\nDigite o endereçõ de {nome_fun}: ").strip().upper(), cpf = input(f"\nDigite o CPF de {nome_fun}: ").strip())
        clear_screen()

    elif res == "2":
        nome = input("\nDigite o nome do funcionario: ").capitalize().strip()
        resu_funcio(nome, endereco = input(f"\nDigite o endereçõ de {nome}: ").strip().upper(), cpf = input(f"\nDigite o CPF de {nome}: ").strip())
        clear_screen()
          
    elif res == "3":
        if clientes == []:
            clear_screen()
            print(f"\n{'-' * 5} CLIENTES {'-' * 5}")
            print("\nLISTA DE CLIENTES VAZIA")
            input("\nContinue...")
            clear_screen()
        else:
            clear_screen()
            print(f"\n{'-' * 5} CLIENTES {'-' * 5}")
            for i in range(len(clientes)):
                print(f"\nNOME: {clientes[i][0]}\nENDEREÇO: {clientes[i][1]}\nCPF: {clientes[i][2]}")
                print(f"\n{'-' * 5}")
            input("\nContinue...")
            clear_screen()

    elif res == "4":
        if funcionario == []:
            clear_screen()
            print(f"\n{'-' * 5} FUNCIONARIOS {'-' * 5}")
            print("\nLISTA DE FUNCIONARIOS VAZIA")
            input("\nContinue...")
            clear_screen()

        else:
            clear_screen()
            print(f"\n{'-' * 5} FUNCIONARIOS {'-' * 5}")
            for i in range(len(funcionario)):
                print(f"\nNOME: {funcionario[i][0]}\nENDEREÇO: {funcionario[i][1]}\nCPF: {funcionario[i][2]}")
                print(f"\n{'-' * 5}")
            input("\nContinue...")
            clear_screen()
        
    else:
        clear_screen()
        print("OPÇÃO INVALIDA!!")
        dec = True

        

      

       





























