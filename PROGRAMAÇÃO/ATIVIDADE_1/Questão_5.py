numero = int(input("Digite um número: "))
primo = True
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False
        break
if primo == True and numero > 1:
    print(numero,"é primo")
else:
    print(numero,"Não é primo")