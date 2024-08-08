def cambio(real):
    if estado == "DOLAR" or estado == "D":
        return  0.18 * real 
    elif estado == "EURO" or estado == "E":
        return 0.16 * real 
    elif estado == "ARGENTINO" or estado == "A":
        return 0.0061 * real   
        
estado = input("Digite o estado para qual você quer fazer a converção do real: ").upper()
valor = float(input("Digite o valor em real: "))


print(f"{cambio(valor):.2f}")