wiek = 14
wzrost = 150
czy_jest_opiekun = 'Tak'
if wiek <= 18 and wzrost >= 120 and czy_jest_opiekun == 'Tak':
    print('Czy można wpuścić gościa: True')
elif wiek >12 and wzrost >=160:
    print('Czy można wpuścić gościa: True')
else:
    print('Czy można wpuścić gościa: False')