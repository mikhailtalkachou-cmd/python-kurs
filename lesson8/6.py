class BladPrzetwarzaniaDanychError(Exception):
    """Wyjątek rzucany, gdy wystąpi błąd przetwarzania danych."""
    pass

def przetworz_dane(dane):
    """
    Przetwarza słownik, łapie KeyError i rzuca BladPrzetwarzaniaDanychError.
    """
    log_file = None
    try:
        # Przykładowe operacje na słowniku
        log_file = open("log.txt", "a", encoding="utf-8")
        imie = dane['imie']
        nazwisko = dane['nazwisko']
        tel = dane['tel']
        
        print(f"Przetwarzanie: {imie} {nazwisko}, Tel: {tel}")
        return True

    except KeyError as e:
        # 2. Logowanie błędu (e to brakujący klucz)
        log_file.write(f"Wystąpił błąd: {e}\n")
        
        # 3. Rzucenie nowego wyjątku z informacją o kluczu
        raise BladPrzetwarzaniaDanychError(f"Błąd przetwarzania: brak wymaganego klucza {e}") from e
    finally:
        log_file.close()



dane_poprawne = {'imie': 'Michal', 'nazwisko': 'Tol', 'tel': '789789789'}
dane_bledne = {'imie': 'Anna', 'nazwisko': 'Nowak'}

print("--- Test 1: Poprawne dane ---")
przetworz_dane(dane_poprawne)
#print("\ntest bledny")
#przetworz_dane(dane_bledne)

print("\n--- Test 2: Błędne dane ---")
try:
    przetworz_dane(dane_bledne)
except BladPrzetwarzaniaDanychError as e:
    print(f"Złapano własny wyjątek: {e}")