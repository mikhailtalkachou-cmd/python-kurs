samoglski = input("napisz zdanie: ")

for i in samoglski:
    if i not in "aeiouy":
        continue
    else:
        print(i)