def soma (num1, num2):
    return (num1 + num2)

def sub (num1, num2):  
    return (num1 - num2)

def mult (num1, num2):  
    return (num1 * num2)

recebe = []
opera = "+-*"
num = "0123456789"

alfa = "qwertyuiopasdfghjklzxcvbnm"

compi = input("Soma e Subtração? ").upper()

if compi[0] == "S":
    for i in range(2):
        res = input("\nInforme o número: ")
        if res not in alfa:
            recebe.append(int(res))
        else:
            pritn("Erro na digitação!!")
        
    print(f"\nRESULTADO:\nSoma: {soma(recebe[0],recebe[1])}\nSubtração: {sub(recebe[0],recebe[1])}")   
    
elif compi[0] == "N":
    operador = input("\nDigite um operador matematico: ")
    if operador in opera:
        for i in range(2):
            res = input("\nInforme o número: ")
            if res not in alfa:
                recebe.append(int(res))
            
            else:
                pritn("Erro na digitação!!")
            
        if operador == "+":
            print(f"\nRESULTADO: {soma(recebe[0],recebe[1])}")
                
        elif operador == "-":
            print(f"\nRESULTADO: {sub(recebe[0],recebe[1])}")
                
        elif operador == "*":
            print(f"\nRESULTADO: {mult(recebe[0], recebe[1])}")     
   
        else:
            print("\nErro na digitação!!")
   
    else:
            print("\nErro na digitação!!")
      

else:
    print("\nErro na digitação!!")

print()