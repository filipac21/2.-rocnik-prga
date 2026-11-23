# d20_chyba_seznam.py — NAJDI DVĚ CHYBY: má spočítat čísla větší než 10 (správně 2)
#
# PŘEDPOVĚĎ: co vypíše tak, jak je? Pak najdi obě chyby a oprav.
#
# >>> KÓD
cisla = [4, 12, 8, 30, 10]
pocet = 0
for i in range(len(cisla)):
    if i > 10:
        pocet = 1
print("větších než 10:", pocet)
# <<< KÓD
#
# PROČ: i je index (0 až 4), ne hodnota; porovnávat se má cisla[i]. A
# pocet = 1 není počítadlo, počítadlo je pocet = pocet + 1. Oba omyly
# program nespadne, jen tiše vypíše nesmysl. To je horší než chyba.
#
# ZKUS: po opravě přepiš cyklus na for c in cisla: (bez indexu). Který
# zápis je čitelnější, když index nepotřebuješ?
