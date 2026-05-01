from pathlib import Path

# Definiujemy główny katalog projektu
project_root = Path("Projekt")

# Definiujemy listę podkatalogów do utworzenia
subdirectories = ["src", "data", "docs"]

# Tworzymy folder główny (parents=True tworzy też katalogi nadrzędne,
# jeśli trzeba, exist_ok=True nie wyrzuca błędu, jeśli folder już istnieje)
project_root.mkdir(exist_ok=True)

# Tworzymy podkatalogi
for sub in subdirectories:
    (project_root / sub).mkdir(exist_ok=True)
    print(f"Utworzono folder: {project_root / sub}")

print("\nStruktura projektu została utworzona.")