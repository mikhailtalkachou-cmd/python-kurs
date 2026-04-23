liczby = list(range(1,31))

def czy_perwsza(n):
    if n == 0 or n == 1:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return False
    return True
    
lista_przefiltrowana = list(filter(czy_perwsza, liczby))

print(lista_przefiltrowana)
#print(liczby)