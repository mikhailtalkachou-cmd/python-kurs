class WiekNiepoprawnyError(Exception):
    """Własny wyjątek dla niepełnoletnich użytkowników."""
    pass

wiek = int(input("Wprowadz swoj wiek: "))

def rejestruj_uzytkownika(wiek):
    if wiek < 18:
        raise WiekNiepoprawnyError(f"Wiek {wiek} jest niewystarczający do rejestracji.")
    print("Użytkownik zarejestrowany pomyślnie!")

# Obsługa wyjątku
try:
    rejestruj_uzytkownika(wiek)
except WiekNiepoprawnyError as e:
    print(f"Błąd: {e}")