data = input("Digite a data: dd/mm/aaaa ")
num = "0123456789"

dia = data[0:2] 
mes = data[3:5]
ano = data[6:10]

if int(dia) <= 31 and int(mes) <= 12 and int(ano) <= 2024:
    print("Data VALIDA!!!!")

else:
    print("Data Invalida!")
    


    
    