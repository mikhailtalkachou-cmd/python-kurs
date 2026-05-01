def odczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            tresc = plik.read()
            return f"istnieje {tresc}"
    except FileNotFoundError:
        return "Błąd: Plik nie istnieje."
    except PermissionError:
        return "Błąd: Brak uprawnień do odczytu tego pliku."
    except Exception:
        return f"Wystąpił nieoczekiwany błąd"

print(odczytaj_plik("12.txt"))