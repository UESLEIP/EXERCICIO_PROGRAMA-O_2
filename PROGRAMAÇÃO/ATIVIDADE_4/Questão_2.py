class ContaBancaria:
    def __init__(self):
        self.titular = "Ueslei Pereira"
        self.saldo = 500
        self.numero_conta = 123
        self.tipo_conta = "poupanca"
        
    def depositar(self, valor):
        self.saldo += int(valor)
        print(f"Valor de {valor} reais foi depositado na conta {self.numero_conta}.")
    
    def sacar(self, valor):
        if int(valor)  <= self.saldo and int(valor)  >= 1:
            self.saldo -= int(valor) 
            print(f"Saldo sacado com sucesso: {valor}")

        elif int(valor)  == 0:
            print("Valor de saque é 0.")

        else:
            print("Valor inválido!")
    
    def transferir(self, valor):  
        if int(valor)  <= self.saldo and int(valor)  >= 1:
            self.saldo -= int(valor) 
            print(f"Saldo transferido com sucesso: {valor}")
        elif int(valor)  == 0:
            print("Valor de transferência é 0.")
        else:
            print("Valor inválido!")

    def verificar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


conta = ContaBancaria()


form = "\n----- Caixa Econômica! -----\n\n1 - DEPOSITAR\n2 - SACAR\n3 - TRANSFERIR\n4 - VERIFICAR SALDO\n\n\nOpção:"


deci = "a"
while deci == "a":
    recebe = input(form)
    if recebe == '1':
        valor = input("Digite o valor a ser depositado: ")
        conta.depositar(valor)
    elif recebe == "2":
        valor = input("Digite o valor a sacar: ")
        conta.sacar(valor)
    elif recebe == "3":
        valor = input("Digite o valor a transferir: ")
        conta.transferir(valor)
    elif recebe == "4":
        conta.verificar_saldo()
    else:
        print("Opção inválida.")

    conti = input("Deseja continuar? (S/N) ").strip().upper()
    if conti == "S" or conti == "SIM":
        continue
    else:
        deci = "b"
