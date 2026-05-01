import json

konfiguracja = {
    "uzytkownik": "admin",
    "motyw": "ciemny",
    "rozdzielczosc": [1920, 1080],
    "powiadomienia": True,
    "wiek ": 20
}

# Zapis do pliku confing.json
with open("confing.json", "w", encoding="utf-8") as plik:
    json.dump(konfiguracja, plik, indent=4, ensure_ascii=False)

print("Konfiguracja została zapisana do pliku config.json")