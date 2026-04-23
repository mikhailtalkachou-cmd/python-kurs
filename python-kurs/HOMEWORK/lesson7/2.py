oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}
oceny_sorted = sorted(oceny.items(), key=lambda x:x[1], reverse=True)

print(oceny_sorted)

print(dict(oceny_sorted))