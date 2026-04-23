from functools import reduce

lista = [1, 2, 3, 4, 5]

wynik = reduce(lambda akkum, x: akkum * x, lista)
print(wynik)