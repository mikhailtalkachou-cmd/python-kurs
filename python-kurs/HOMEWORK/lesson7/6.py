
def  stworz_licznik(n):
    #licznik = 0 
    
    def zwekszony_licz_o_jeden():
        nonlocal n
        n += 1
        return n 
    return zwekszony_licz_o_jeden

moj_licznik = stworz_licznik(2)
print(moj_licznik())
print(moj_licznik())