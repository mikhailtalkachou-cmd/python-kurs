imie = input("Wprowadź swoje imię: ")
rok_urodzenia = int(input("wprowadź rok urodzenia: "))

def poprawny_wiek (x):
    if rok_urodzenia >= 1900 and rok_urodzenia <= 2026:
        return(x)
    elif rok_urodzenia >= 0 and rok_urodzenia <= 26:
        return(x+2000)
    elif rok_urodzenia >= 27 and rok_urodzenia <= 99:
        return(x+1900)
    
wiek = 2026 - poprawny_wiek(rok_urodzenia)
#zmienna wiek musi byc ZA funkc inaczej nie dziala
print(f"Cześć, {imie}! W 2026 roku będziesz mieć około {wiek} lat.")
