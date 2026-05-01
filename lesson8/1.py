def calculator():
    
    while True:
        try:
            #wprowadzanie  danych
            perwsza_liczba = input("Podaj perwsza liczbe: ")
            if perwsza_liczba.lower() == 'q': break
            a = float(perwsza_liczba)
            operacja = input("Podaj dzialanie (+,-,*,/): ")
            druga_liczba = input("Podaj druga liczbe: ")
            b = float(druga_liczba)
            #operacja
            if operacja == "+":
                wynik = a + b
            elif operacja == "-":
                wynik = a - b
            elif operacja == "*":
                wynik = a * b
            elif operacja == "/":
                wynik = a / b
                #tytai  ZeroDivisionError przy dzel na 0
            else:
                print("Wprowadzona bledna operacja")
                continue
        except ValueError:
            print("Bland. Wprowadz liczbe!")
        except ZeroDivisionError:
            print("Bland. Nie morzna dzielic przez 0")
        else:
            print(f"Otszymamy:{a}{operacja}{b}={wynik}")
        finally:
            print("Kolejna operacja ...")
    
        
calculator()    
    
