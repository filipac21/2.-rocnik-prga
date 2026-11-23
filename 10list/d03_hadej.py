import random
tajne = random.randint(1, 100)
tip = int(input("Tip: "))
pokusy = 1
while tip != tajne:
    if tip < tajne:
        print("Více")
    else:
        print("Méně")
    tip = int(input("Tip: "))
    pokusy = pokusy + 1
print("Správně na", pokusy, "pokusů")