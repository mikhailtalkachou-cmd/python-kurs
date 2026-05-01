import json

with open("confing.json","r", encoding="utf-8") as plik:
    plik_odczytany = json.load(plik)
    
print(plik_odczytany)
print(plik_odczytany["motyw"])
