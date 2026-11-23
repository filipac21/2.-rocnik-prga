# d05_continue.py — continue: přeskoč tohle kolo, pokračuj dalším
#
# PŘEDPOVĚĎ: která čísla se vypíší?
#
# >>> KÓD
for c in [4, 8, 15, 16, 23, 42]:
    if c % 2 == 1:                  # zbytek po dělení dvěma 1 = liché
        continue                    # liché přeskoč: zpátky na začátek cyklu
    print(c, end=" ")
# <<< KÓD
#
# PROČ: continue neukončí cyklus, jen přeskočí zbytek těla pro aktuální
# hodnotu. Totéž jde napsat i bez continue (if c % 2 == 0: print(c)),
# ale u delšího těla je continue přehlednější: „tohle mě nezajímá, dál“.
#
# ZKUS: přepiš program bez continue tak, aby vypsal totéž.
