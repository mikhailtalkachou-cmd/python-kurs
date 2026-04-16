def cena_ulg (x):
    return(x/2)

cena_norm = 100
wiek = int(input("Ilie masz lat?: "))
czy_jest_studentem = bool(input("Czy jesteś studentem?: "))

if (wiek <= 18 and wiek >=0) or czy_jest_studentem == True:
    print("Do zapłaty ", cena_ulg(cena_norm), " zł.")
else:
    print("Do zapłaty ", cena_norm, " zł. ")