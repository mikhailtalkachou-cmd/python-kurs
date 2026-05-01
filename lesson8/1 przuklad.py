def kalkulator():
    print("--- Prosty Kalkulator (wpisz 'q' zamiast liczby, aby wyjść) ---")
    
    while True:
        try:
            # Pobranie danych
            wejscie1 = input("\nPodaj pierwszą liczbę: ")
             
            liczba1 = float(wejscie1)
            
            operacja = input("Podaj operację (+, -, *, /): ")
            
            wejscie2 = input("Podaj drugą liczbę: ")
            if wejscie2.lower() == 'q': break
            liczba2 = float(wejscie2)
            
            # Wykonanie obliczeń
            if operacja == '+':
                wynik = liczba1 + liczba2
            elif operacja == '-':
                wynik = liczba1 - liczba2
            elif operacja == '*':
                wynik = liczba1 * liczba2
            elif operacja == '/':
                # ZeroDivisionError jest obsługiwane przez próbę dzielenia
                wynik = liczba1 / liczba2
            else:
                print("Nieobsługiwana operacja!")
                continue
                
        except ValueError:
            # Obsługa błędu, gdy użytkownik nie poda liczby
            print("BŁĄD: Wprowadzono nieprawidłowe dane! Oczekiwano liczby.")
        except ZeroDivisionError:
            # Obsługa dzielenia przez zero
            print("BŁĄD: Nie można dzielić przez zero!")
        else:
            # Wyświetlenie wyniku, jeśli nie wystąpił błąd
            print(f"Wynik: {liczba1} {operacja} {liczba2} = {wynik}")
        finally:
            # Blok uruchamiany zawsze
            print("Kolejna operacja...")

if __name__ == "__main__":
    kalkulator()