# d07_binarne.py — while a dělení dvěma: číslo na jedničky a nuly
#
# PŘEDPOVĚĎ: jak se zapíše 13 dvojkově? (13 = 8 + 4 + 1.)
#
# >>> KÓD
n = 13
bity = ""
while n > 0:
    bity = str(n % 2) + bity        # zbytek po dělení dvěma přidej ZLEVA
    n = n // 2                      # a číslo zmenši na polovinu (celočíselně)
print(bity)
# <<< KÓD
#
# PROČ: 13 % 2 = 1, 13 // 2 = 6; 6 % 2 = 0, 6 // 2 = 3; 3 % 2 = 1, 3 // 2 = 1;
# 1 % 2 = 1, 1 // 2 = 0 → konec. Zbytky odzadu: 1101. Přesně tohle dělá
# počítač s každým bajtem obrázku z PRGA-09: 255 je 11111111.
#
# ZKUS: n = 192, n = 255, n = 256. Kolik má 256 číslic a proč je to o jednu
# víc než 255?
