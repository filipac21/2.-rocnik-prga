# Funkce 6 — graf doopravdy: knihovna matplotlib
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# matplotlib je knihovna na grafy, kterou používají vědci i firmy. Není
# v Pythonu od začátku: nainstaluje se v terminálu příkazem
#     pip install matplotlib
# (v terminálu, ne v Pythonu; chvíli to trvá). Když to nejde (bez práv,
# bez internetu), tenhle program přeskoč: grafy z programu 3 stačí.
# Program vyrobí dva seznamy (x a y), předá je knihovně a ta otevře okno.
#
# >>> KÓD — tohle opisuješ
import math
import matplotlib.pyplot as plt

xs = []                        # prázdné seznamy, budeme je plnit
ys = []
for i in range(-50, 51):       # i = -50 … 50
    x = i / 10                 # x = -5,0 … 5,0 po desetinách (101 bodů)
    xs.append(x)               # append = přidej na konec seznamu
    ys.append(x * x)           # zkus: 2 * x + 1, math.sin(x), 1 / (1 + math.exp(-x)), max(0, x)

plt.plot(xs, ys)               # nakresli čáru body (xs[0], ys[0]), (xs[1], ys[1]), …
plt.title("y = x * x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()                     # otevře okno; zavři ho, program pak skončí
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# import matplotlib.pyplot as plt
#     Z knihovny matplotlib si bereme část pyplot a říkáme jí krátce plt.
#     Když řádek spadne na ModuleNotFoundError, knihovna není
#     nainstalovaná: pip install matplotlib v terminálu.
#
# xs = []   ys = []
#     Prázdné seznamy. Do seznamu se přidává metodou append (na konec).
#     V programu 1 byl seznam napsaný ručně, tady si ho program vyrobí.
#
# for i in range(-50, 51):  x = i / 10
#     range dává jen celá čísla. Dělením deseti z nich uděláme desetiny:
#     101 bodů místo 11, čára je hladká.
#
# plt.plot(xs, ys)
#     Spojí body čarou. Dvě čáry v jednom grafu: zavolej plot dvakrát,
#     každý s label="…", a před show() přidej plt.legend().
#
# plt.show()
#     Teprve tohle okno otevře. Všechno před tím jen chystá.
#
# Zkus: plt.plot(xs, ys, marker="o") ukáže i body.
# Zkus: ys2 se sigmoidem a plt.plot(xs, ys2, label="sigmoid").
