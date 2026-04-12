# 1 - true , 0 - false
mam_prawo_jazdy = input("Czy masz prawo jazdy? :") == "1"
mam_auto = input("Czy masz auto? :") == "1"

print(f"Morzesz pojechać w kazdej chwili: {mam_prawo_jazdy and mam_auto} (operacja AND)")
print(f"Teorytycznie mozesz jezdzić: {mam_prawo_jazdy or mam_auto} (operacja OR)")