def stworz_profil(imie: str, **dane_dodatkowe) -> dict:
    prof_urzytkownika = {"imie":imie}
    prof_urzytkownika.update(dane_dodatkowe)
    return prof_urzytkownika

print(stworz_profil(imie = "Michal", wiek = 30, stan = "kawaler", prawo_jazdy = True))