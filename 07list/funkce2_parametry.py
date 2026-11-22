# Funkce 2 — přímka s parametry: a a b zadá uživatel
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# V tabulce jsi měl a a b v buňkách a vzorec se na ně odkazoval ($I$2).
# Tady se na ně program zeptá: input() vrátí text, float() z něj udělá
# desetinné číslo. Pak je to stejná tabulka jako v programu 1, jen
# s range místo seznamu a s desetinnými y.
#
# >>> KÓD — tohle opisuješ
a = float(input("a (sklon): "))
b = float(input("b (posun): "))
krok = int(input("Krok (celé číslo): "))

print(f"y = {a} * x + {b}")
print("    x        y")
for x in range(-5, 6, krok):
    y = a * x + b
    print(f"{x:5}  {y:7.1f}")
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# a = float(input("a (sklon…): "))
#     Čti zevnitř: input() vypíše otázku a počká na Enter; vrátí TEXT.
#     float() ten text převede na desetinné číslo. Pozor: piš 2.5 s tečkou.
#     Napíšeš-li 2,5 s čárkou, float spadne na ValueError (chybu čti
#     odspodu, poslední řádek říká proč).
#
# range(-5, 6)
#     Posloupnost celých čísel od -5 do 5. Druhé číslo je „kam až, ale
#     bez“. Třetí číslo je krok: range(-5, 6, 2) dá -5, -3, -1, 1, 3, 5.
#
# {y:7.1f}
#     Sedm míst, jedno desetinné. Bez toho by se u některých hodnot
#     vypsalo třeba 3.0000000000000004 (desetinná čísla v počítači nejsou
#     přesná, viz říjen).
#
# Zkus: a = 0 (vodorovná čára, y je pořád b), a = -1 (klesá), b = 10
# (posune nahoru). V tabulce jsi měnil buňku, tady odpovídáš na otázku.
# Stejný princip, jiný způsob zadání.
