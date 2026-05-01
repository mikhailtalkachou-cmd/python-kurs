def szukaj_w_logach():
    plik_wejsciowy = 'log.txt'
    plik_wyjsciowy = 'wyniki_wyszukiwania.txt'

    # Pobranie szukanego słowa od użytkownika
    slowo = input("Podaj słowo do wyszukania: ")

    if not slowo:
        print("Nie podano słowa. Zamykanie programu.")
        return

    try:
        # Otwieramy plik logów do odczytu i nowy plik do zapisu
        with open(plik_wejsciowy, 'r', encoding='utf-8') as infile, \
             open(plik_wyjsciowy, 'w', encoding='utf-8') as outfile:
            
            licznik = 0
            # Przetwarzanie pliku linia po linii (efektywne dla dużych plików)
            for line in infile:
                if slowo in line:
                    outfile.write(line)
                    licznik += 1
            
            print(f"Zakończono. Znaleziono {licznik} linii.")
            print(f"Wyniki zapisano w: {plik_wyjsciowy}")

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {plik_wejsciowy}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    szukaj_w_logach()