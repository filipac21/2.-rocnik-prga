# d19_chyba_while.py — NAJDI CHYBU: má vypsat 1 až 5 a pak "hotovo 6"
#
# PŘEDPOVĚĎ: co program vypíše tak, jak je? Pak najdi chybu a oprav.
#
# >>> KÓD
i = 1
while i < 5:
    print(i)
    i = i + 1
print("hotovo", i)
# <<< KÓD
#
# PROČ: chyba „o jedničku“ je nejčastější chyba u cyklů vůbec: < místo <=.
# Vždycky si dosaď krajní hodnotu (tady 5) a zeptej se, jestli podmínka
# ještě platí.
#
# ZKUS: oprav podmínku. Pak udělej druhou, horší chybu schválně: odsaď
# řádek i = i + 1 ven z cyklu (na začátek řádku) a spusť. Program se
# nezastaví; ukonči ho Ctrl+C a vysvětli sousedovi proč.
