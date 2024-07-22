#Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
#Escreva um programa que pergunta a situação do usuário (se é idoso, se é
#gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
#prioridade ou não.

situ = input("Digite a sua situação: ").upper().upper()
if situ == "IDOSO" or situ == "GESTANTE" or situ == "PCD":
    print("Você tem acesso a fila de prioridade")

else:
    print("Não é nenhum desses")  