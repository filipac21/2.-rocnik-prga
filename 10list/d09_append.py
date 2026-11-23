# d09_append.py — seznam roste a zmenšuje se: append, remove
#
# PŘEDPOVĚĎ: co je v seznamu na konci a kolik toho je?
#
# >>> KÓD
nakup = []                          # prázdný seznam
nakup.append("chleba")              # přidej na konec
nakup.append("mléko")
nakup.append("máslo")
nakup.remove("mléko")               # odeber podle hodnoty (první výskyt)
print(nakup, len(nakup))
# <<< KÓD
#
# PROČ: append přidává vždy na konec, remove hledá hodnotu a smaže ji.
# Zapamatuj si: nakup = nakup.append("x") je chyba, append nic nevrací
# (vrátí None) a seznam bys tím přepsal na None.
#
# ZKUS: nakup.remove("rohlík"). Jaká chyba? Jak se zeptat předem, jestli
# tam rohlík je? (Nápověda: d10.)
