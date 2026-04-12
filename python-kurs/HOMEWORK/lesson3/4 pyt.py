imie = input("Wprowadź swoje imię: ")
rok_urodzenia = 1987
#rok_urodzenia = input("Wprowadź wiek: ") 
# (mimo tego ze wiek wprowadzany cyframi python widzi jak str, musze wpisac:
# rok_urodzenia = int(input("Wprowadź wiek: "))
 
#dla czego nie działa? 
def poprawny_wiek (x):
    if 1900 <= x <= 2026:
        return(x)
    elif 26 < x == 99:   
        return(x+1900)
    elif 0 <= x == 26 :
        return(x+2000)
    else:
        print("Wprowadź poprawny wiek!")

print(poprawny_wiek(rok_urodzenia))
#print(f"Cześć, {imie}! W 2026 roku będziesz mieć około {wiek} lat.")
