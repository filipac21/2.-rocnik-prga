# b1_seznam.py — seznam čísel a cyklus: počet, součet, největší, kolik jich je nad hranicí
#
# JAK TO FUNGUJE
# --------------
# Seznam je řada hodnot v hranatých závorkách. Cyklus for projde hodnoty
# jednu po druhé. To je všechno, co dnes potřebuješ: obrázek bude taky jen
# seznam čísel, akorát jich bude 172 854.
#
# Spuštění:  python b1_seznam.py
#
# >>> KÓD — tohle opisuješ
teploty = [12, 15, 9, 21, 18, 7, 25]        # seznam sedmi čísel

print("počet:", len(teploty))              # len = délka seznamu
print("součet:", sum(teploty))             # sum = součet
print("průměr:", sum(teploty) / len(teploty))
print("první:", teploty[0], "  poslední:", teploty[6], "  nebo:", teploty[-1])

nejvetsi = teploty[0]                      # zatím největší je první
for t in teploty:                          # t je postupně 12, 15, 9, …
    if t > nejvetsi:
        nejvetsi = t
print("největší:", nejvetsi, "  (max umí totéž:", max(teploty), ")")

pocet = 0
for t in teploty:
    if t > 15:
        pocet = pocet + 1                  # počítadlo: +1 za každý den nad 15
print("dní nad 15 °C:", pocet)

for i in range(len(teploty)):              # i = 0, 1, 2, … 6: index do seznamu
    print(i, teploty[i], "#" * teploty[i])  # text krát číslo = graf (PRGA-03)
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# teploty[0] je první hodnota, teploty[6] sedmá, teploty[-1] poslední.
#     Index začíná nulou. teploty[7] spadne: IndexError, seznam má jen 7 prvků.
# for t in teploty:   projde HODNOTY.      for i in range(len(teploty)):   projde INDEXY.
#     Druhý způsob potřebuješ, když chceš vědět, kolikátý prvek to je, nebo
#     prvek změnit: teploty[i] = 0.
# pocet = pocet + 1   je počítadlo. Před cyklem 0, v cyklu +1, po cyklu výsledek.
#
# Zkus: přidej do seznamu osmé číslo. Spočítej, kolik dní bylo POD 10.
# Zkus: vypiš jen každou druhou teplotu: for i in range(0, len(teploty), 2):
