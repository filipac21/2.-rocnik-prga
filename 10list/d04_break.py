# d04_break.py — break: vyskoč z cyklu hned, nečekej na konec řady
#
# PŘEDPOVĚĎ: které řádky se vypíší?
#
# >>> KÓD
cisla = [4, 8, 15, 16, 23, 42]
for c in cisla:
    if c > 10:
        print("první větší než 10:", c)
        break                       # konec cyklu, zbytek seznamu se nečte
    print("malé:", c)
# <<< KÓD
#
# PROČ: break ukončí cyklus okamžitě. Hodí se při hledání: jakmile máš, co
# jsi hledal, nemá smysl pokračovat. Funguje ve for i ve while.
#
# ZKUS: smaž řádek s break. Co se změní? A co když žádné číslo > 10 není?
