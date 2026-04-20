POZIOM_DOSTEMPU = "user"

def zmiana():
    POZIOM_DOSTEMPU = "admin"
    print(f"Wewnatrz funkcji: {POZIOM_DOSTEMPU}")
    
print(f"Na zewnatrz: {POZIOM_DOSTEMPU}")

zmiana()