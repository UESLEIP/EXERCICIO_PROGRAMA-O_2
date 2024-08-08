vogal = "AEIOU"
print()
letra = input("Digite um letra: ").upper()
if len(letra) != 1 :
    print()
    print("ERRO!! Digite somente uma letra!")
elif letra in vogal:
    print()
    print(f"{letra} é vogal")
else:
    print()
    print(f"{letra} é consoante")
