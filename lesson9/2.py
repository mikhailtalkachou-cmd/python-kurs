nazwa_pliku = input("Podaj nazwę pliku do odczytania (np. tekst.txt): ")

try:
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        tresc = plik.read()
            
        slowa = tresc.split()
        liczba_slow = len(slowa)
            
        print(f"Plik '{nazwa_pliku}' zawiera {liczba_slow} słów.")
        
        print(tresc)

except FileNotFoundError:
        print(f"Błąd: Plik o nazwie '{nazwa_pliku}' nie istnieje.")
except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
