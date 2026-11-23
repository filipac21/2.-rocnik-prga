# d13_zmena.py — změna prvků: přes index ano, přes kopii v cyklu ne
#
# PŘEDPOVĚĎ: jaký seznam se vypíše?
#
# >>> KÓD
ceny = [100, 250, 80]
for i in range(len(ceny)):
    ceny[i] = ceny[i] * 2           # přepiš prvek na indexu i
print(ceny)
# <<< KÓD
#
# PROČ: ceny[i] = … sáhne do seznamu. Častá chyba (dělá ji i AI):
#     for c in ceny:
#         c = c * 2
# nezmění nic, protože c je jen kopie hodnoty, ne místo v seznamu.
#
# ZKUS: přepiš cyklus na for c in ceny: c = c * 2 a vypiš ceny. Pak zkus
# třetí cestu: nový seznam a append.
