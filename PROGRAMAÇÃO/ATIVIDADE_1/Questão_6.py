perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

cont = 0
print()
for i in perguntas:
    res = input(f"{i} S/N: ")
    if res != int:
        for im in res[0]:
            if cont <= 5:
                if im.upper() == "S":
                    cont = cont + 1
                elif im.upper() == "N": 
                    cont = cont
if cont == 2:
    print("Essa pessoa é suspeita!") 

elif cont == 3 or cont == 4:
    print("Essa pessoa é cúmplice")

elif cont == 5:
    print("Essa pessoa e o ASSASSINO")

elif cont == 0:
        print("Essa pessoa é INOCENTE")
else:
    print("ERRO!!!!!!")