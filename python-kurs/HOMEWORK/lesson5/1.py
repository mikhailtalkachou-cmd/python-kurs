wiek = int(input("Wprowadź swoj wiek: "))
    
if wiek == 0 or wiek == 1:
    print("Niemowlę")
elif wiek >= 2 and wiek <=12:
    print("Dziecko")
elif wiek >= 13 and wiek <=17:
    print("Nastolatek")
elif wiek >= 18 and wiek <= 64:
    print("Dorosły")
elif wiek >= 65 and wiek <= 120:
    print("Senior")
else:
    print("Wprowadź poprawny wiek")

