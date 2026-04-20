def sprawdz_haslo(haslo: str) -> bool:
    if len(haslo) < 8:
        return False
    for i in haslo:
        if i is "0123456789":
            continue
        else:
            return False
    for j in haslo:
        if j is "QWERTYUIOPASDFGHJKLZXCVBNM":
            return True
        else:
            return False
        
print(sprawdz_haslo("jN8888888888hjh"))