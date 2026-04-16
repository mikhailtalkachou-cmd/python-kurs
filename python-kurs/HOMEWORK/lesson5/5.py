i = 0
j = 0 

for j in range(6):
    for i in range(6):
            if j < 6:
                print(i*j)
                i += 1
            break
if i < 6:
    print(i*j)
    i += 1
    
