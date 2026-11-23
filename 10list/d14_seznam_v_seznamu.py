# d14_seznam_v_seznamu.py — seznam seznamů: dva indexy, řádky
#
# PŘEDPOVĚĎ: první řádek má tři čísla, pak dva řádky s jedním. Jaká?
#
# >>> KÓD
radky = [[1, 2, 3], [4, 5, 6]]
print(radky[1][0], len(radky), len(radky[0]))
for r in radky:
    print(sum(r))
# <<< KÓD
#
# PROČ: radky[1] je druhý vnitřní seznam [4, 5, 6], radky[1][0] jeho první
# prvek. len(radky) je počet řádků, len(radky[0]) počet sloupců. Mřížka 8×8
# z PRGA-08 byla přesně tohle: osm seznamů po osmi číslech.
#
# ZKUS: vypiš součet každého sloupce (nápověda: for j in range(3): …
# radky[0][j] + radky[1][j]).
