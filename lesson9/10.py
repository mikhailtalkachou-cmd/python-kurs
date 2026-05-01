# Mini-projekt: Lista zadań: Stwórz prostą aplikację do zarządzania listą zadań. Program
# powinien:
# Przy starcie próbować wczytać zadania z pliku zadania.json .
# Pozwalać użytkownikowi dodać nowe zadanie.
# Pozwalać wyświetlić wszystkie zadania.
# Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku
# zadania.json


import json

# Nazwa pliku do przechowywania danych
plik_z_zadaniami = 'zadania.json'

def wczytaj_zadania():
    """Wczytuje zadania z pliku JSON. Jeśli plik nie istnieje, zwraca pustą listę."""
    if plik_z_zadaniami:
        with open(plik_z_zadaniami, 'r', encoding='utf-8') as plik:
            try:
                return json.load(plik)
            except json.JSONDecodeError:
                return []
            except FileNotFoundError as e:
                print(f"Wystopil nieoczekiwany blad: {e}")    
    return []

def zapisz_zadania(zadania):
    """Dopisuje listę zadań do pliku JSON."""
    with open(plik_z_zadaniami, 'a', encoding='utf-8') as plik:
        json.dump(zadania, plik, indent=4, ensure_ascii=False)
    print("...zadania zostały zapisane.")


zadania = wczytaj_zadania()

while True:
    print("\n--- TWOJA LISTA ZADAŃ ---\n___wybiez co bys chcial zrobic___")
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Wyjdź i zapisz")
    
    wybor = input("Wybierz opcję (1-3): ")

    if wybor == '1':
        if not zadania:
            print("\nLista jest pusta.")
        else:
            print("\nZadania do wykonania:")
            for i, zadanie in enumerate(zadania, 1):
                print(f"{i}. {zadanie}")
    elif wybor == '2':
        nowe_zadanie = input("Wpisz treść zadania: ")
        if nowe_zadanie:
            zadania.append(nowe_zadanie)
            print("Dodano!")
        
    elif wybor == '3':
        zapisz_zadania(zadania)
        print("Koniec programu. Miłego dnia!")
        break
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")