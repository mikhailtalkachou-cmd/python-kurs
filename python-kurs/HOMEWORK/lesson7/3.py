imiona = ["anna", "piotr", "kasia"]

#imiona_wielka_litera = list(map(lambda x: x.upper(), imiona))
#imiona_wielka_litera = list(map(lambda x: x.title(), imiona))
imiona_wielka_litera = list(map(lambda x: x.capitalize(), imiona))

print(imiona_wielka_litera)