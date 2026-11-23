# d11_soucet_rucne.py — součet cyklem a hotovou funkcí; průměr
#
# PŘEDPOVĚĎ: tři hodnoty. Jaké? (Pozor na typ té třetí.)
#
# >>> KÓD
body = [7, 10, 4, 9]
soucet = 0
for b in body:
    soucet = soucet + b             # střádej
print(soucet, sum(body), soucet / len(body))
# <<< KÓD
#
# PROČ: sum dělá přesně to, co cyklus: začne nulou a přičítá. Průměr je
# součet lomeno počet; dělení / vrací vždy desetinné číslo, proto 7.5 a ne 7.
#
# ZKUS: body = [] a spusť. Která hodnota projde a která spadne? Jak se tomu
# vyhnout podmínkou?
