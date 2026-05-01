def oblicz_srednia(lista_ocen):
    assert len(lista_ocen) > 0, "Lista ocen nie może być pusta!"
    return sum(lista_ocen) / len(lista_ocen)

oceny = [3, 5, 4, 2, 5]
oceny_1 = []


print(oblicz_srednia(oceny))
print(oblicz_srednia(oceny_1))