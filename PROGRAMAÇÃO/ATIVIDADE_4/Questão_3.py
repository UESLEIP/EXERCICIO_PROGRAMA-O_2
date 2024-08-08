class produto:
    def __init__(self):
        self.nome = "Copo"
        self.preço = 8.52
        self.quantidade = 10
        self.codigo = 5846

    def calcular_total(self):
        print(self.preço * self.quantidade)

    def atualizar_preco(self):
        digi = float(input("Digite o novo preço: "))
        self.preço = digi
        print(f"O novo preço do produto {self.nome} é: {self.preço}")

    def verificar_disponibilidade(self):
        if self.quantidade >= 0:
            print(f"Disponivel: {self.quantidade}")


produtos = produto()

form = ("\n-----Estoque-----\n\n\n1 - CALCULAR TOTAL\n2 - ATUALIZAR PREÇO\n3 - VERIFICAR DISPONIBILIDADE\n\n\nOpção: ")

deci = input(form)
if deci == "1":
    produtos.calcular_total()
elif deci == "2":
    produtos.atualizar_preco()
elif deci == "3":
    produtos.verificar_disponibilidade()