# d08_index.py — seznam: index od začátku, od konce, výřez, délka
#
# PŘEDPOVĚĎ: čtyři hodnoty na jednom řádku. Jaké?
#
# >>> KÓD
mesta = ["Praha", "Brno", "Ostrava", "Plzeň"]
print(mesta[0], mesta[-1], mesta[1:3], len(mesta))
# <<< KÓD
#
# PROČ: index 0 je první prvek, −1 poslední. Výřez [1:3] vezme indexy 1 a 2
# (konec se nebere), výsledkem je nový seznam. len = počet prvků, ne
# nejvyšší index (ten je len − 1).
#
# ZKUS: mesta[4]. Jaká chyba a proč? Pak mesta[1:], mesta[:2], mesta[::2].
