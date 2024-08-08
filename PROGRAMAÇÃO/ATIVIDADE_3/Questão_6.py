import os
 
def limpar():
    os.system('cls')


def nota(horas):
    soma1 = horas[0] + horas[1]
    soma2 = horas[3] + horas[4]
    if (int(soma1) >= 13 and int(soma1) <= 24) and (int(soma2) >= 0 and int(soma2) <= 59):
        calcu = int(horas[0:2]) - 12
        print(calcu)
        conver = str(calcu)
        if len(conver) == 2:
            resul.append(conver[0])
            resul.append(conver[1])
            print(resul)
        else:
            resul.append(int(conver))
        
    else:
        print("ERRO NA DIGITAÇÃO!!")
    
    return

def prin(no):
    if recebe[2] == ":":
        if len(no) == 1:
            return ("0" + str(no[0])) + recebe[2:5]
        elif len(no) == 2:
            if str(no[0]) + str(no[1]) == "12":
                return "00" + recebe[2:5]
            else:
                return (str(no[0]) + str(no[1])) + recebe[2:5]
    else:       
        print("ERRO NA DIGITAÇÂO!!")
    


n = 0
resul = []
recebe = input("DIGITE A HORAS FORM ")
(nota(recebe))


limpar()
print()
print(f"A notação de {recebe} para 12 horas é: {prin(resul)}")
print()