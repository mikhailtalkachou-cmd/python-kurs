def analiza_listy(lista: list[int]) -> tuple:
    a = max(lista)
    b = min(lista)
    c = sum(lista)
    """Zwraca krotke z min, max wartoscia i sum wartosci z listy"""
    return b, a, c

x = [4, 5, 9, 34, 23]

print(analiza_listy(x))