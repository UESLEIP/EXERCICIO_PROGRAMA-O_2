turno = input("Em que turno você estuda? [M/V/N] ").upper().strip()

for i in range(1):
    if turno == "M":
        print("BOM DIA!")
    elif turno == "V": 
        print("BOA TARDE!")
    elif turno == "N":
        print("BOA NOITE!")
    else:
        for i in turno[0]:
            if i == "M":
                print("BOM DIA!")
            elif i == "V": 
                print("BOA TARDE!")
            elif i == "N":
                print("BOA NOITE!")


