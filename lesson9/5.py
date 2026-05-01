#Masz listę słowników: produkty = [{"nazwa": "Mleko", "cena":
#3.50}, {"nazwa": "Chleb", "cena": 4.20}] . Zapisz te dane do pliku produkty.csv ,
#gdzie pierwszy wiersz to nagłówki ("nazwa", "cena").

import csv

produkty = [
{"Nazwa": "Mleko", "Cena": 3.50},
{"Nazwa": "Chleb", "Cena": 4.20},
]

# Definiujemy nazwę pliku
plik_csv = 'produkty.csv'

# Definiujemy nagłówki (muszą odpowiadać kluczom w słownikach)
naglowki = ["Nazwa", "Cena"]

# Zapisywanie danych do pliku
with open(plik_csv, mode='w', newline='', encoding='utf-8') as file:
    # Tworzymy obiekt DictWriter
    writer = csv.DictWriter(file, fieldnames=naglowki)
    
    # Zapisujemy nagłówki w pierwszym wierszu
    writer.writeheader()
    
    # Zapisujemy dane (wiersze)
    writer.writerows(produkty)

print(f"Dane zostały zapisane do pliku {plik_csv}")
