def maior(num1, num2, num3):
    maior = 0
    if num1 > num2 and num1 > num3:
        maior = num1
    
    elif num2 > num1 and num2 > num3:
        maior = num2
        
    elif num3 > num1 and num3 > num2:
        maior = num3
    
    return maior 

def menor(num1, num2, num3):
    menor = 0

    if num1 < num2 and num1 < num3:
        menor = num1
        
    elif num2 < num1 and num2 < num3:
        menor = num2
        
    elif num3 < num1 and num3 < num2:
        menor = num3
        
    return menor


numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))

print("Maior: ", maior(numero1, numero2, numero3))
print("Menor: ", menor(numero1, numero2, numero3))

