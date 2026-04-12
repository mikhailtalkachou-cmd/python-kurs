imie = 'Michal'
wiek = 38
oceny = [3, 2, 3, 5, 4]
czy_student = True
sred_ocen = sum(oceny)/len(oceny)

def opisz_zmienna(x):
    return f"{x}[{type(x)}]"

for x in (imie, wiek, sred_ocen, czy_student):
    print(opisz_zmienna(x))