# Funkce 3 — graf v terminálu: sloupec z mřížek a hvězdička na pozici
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Graf nepotřebuje žádnou knihovnu. Stačí za každé x vypsat tolik znaků,
# kolik je y: "#" * y. Je to tabulka z programu 1, jen místo čísla y
# vidíš jeho délku. Druhá část kreslí sinus jinak: hvězdičku odsune
# mezerami na pozici (trik z rozcvičky 5 v PRGA-03).
#
# >>> KÓD — tohle opisuješ
import math

print("x * x jako sloupce:")
for x in range(-5, 6):
    y = x * x                       # zkus: 2 * x + 1, abs(x), max(0, x)
    print(f"{x:3} | {y:3} " + "#" * y)

print()
print("sin(x) jako čára:")
for i in range(0, 32):
    x = i * 0.25                    # 0; 0,25; 0,5; … 7,75
    pozice = int(10 + 10 * math.sin(x))   # -1..1  →  0..20
    print(" " * pozice + "*")
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# "#" * y
#     Text krát číslo = opakování (říjen: "a" * 3 je "aaa"). Pro y = 9
#     vznikne devět mřížek. Pro y = 0 prázdný text. Pro záporné y taky
#     prázdný text, nespadne to: proto má 2 * x + 1 vlevo prázdné řádky.
#     "#" * 2.5 ale spadne na TypeError: desetinné y nejdřív zaokrouhli,
#     "#" * round(y).
#
# f"{x:3} | {y:3} " + "#" * y
#     Dva texty slepené plusem: popisek s čísly a sloupec mřížek.
#
# for i in range(0, 32):  x = i * 0.25
#     range umí jen celá čísla, proto počítáme i = 0 … 31 a x z něj
#     vyrobíme násobením. 32 řádků je zhruba jedna a čtvrt vlny.
#
# pozice = int(10 + 10 * math.sin(x))
#     Sinus dává -1 až 1. Krát deset: -10 až 10. Plus deset: 0 až 20. int()
#     usekne desetiny, protože mezer musí být celý počet. Přesně tohle
#     jsi dělal v PRGA-03 s kuličkou.
#
# print(" " * pozice + "*")
#     Tolik mezer, kolik je pozice, a za nimi hvězdička. Řádek pod řádkem
#     vznikne vlna. Osa x tu jde dolů, ne doprava: graf je otočený
#     o 90 stupňů.
#
# Zkus: sigmoid 1 / (1 + math.exp(-x)) je mezi 0 a 1, takže "#" * y dá
# skoro nic. Vynásob čtyřiceti a zaokrouhli: "#" * round(40 * y).
