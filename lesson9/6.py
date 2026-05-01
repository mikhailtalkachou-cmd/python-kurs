import csv

suma_cen = 0.0

with open("produkty.csv", mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    print("\nOdczytane produkty:")
    for row in reader:
        # csv.DictReader czyta wszystko jako string,
        # więc zamieniamy 'cena' na float
        cena = float(row['Cena'])
        suma_cen += cena
        print(f"- {row['Nazwa']}: {cena:.2f} zł")

print(f"\nSuma cen wszystkich produktów: {suma_cen:.2f} zł")