def oblicz_srednia(*args: int) -> float:
    if not args:
        return 0
    summa_ocen = sum(args)
    ilosc_ocen = len(args)
    return summa_ocen / ilosc_ocen

print(oblicz_srednia(2, 3, 3, 2, 5))
print(oblicz_srednia())
