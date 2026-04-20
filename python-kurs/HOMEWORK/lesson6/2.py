def opis_ks(tytul: str, autor: str, rok_wydania: int=2024) -> str:
    return f"Książka '{tytul}' została napisana przez {autor} i wydana w roku {rok_wydania}."

print(opis_ks("Czarny kot", "Andrzej Kobalt", 1980))
print(opis_ks("Harry poter", "Niewiem Kto"))
print(opis_ks("Znachar", rok_wydania = 1937, autor = "Tadeusz Dołega"))