# d03_hadej.py — while s podmínkou od uživatele: opakuj, dokud neuhodne
#
# PŘEDPOVĚĎ: uživatel napíše postupně 3, 9, 7. Co program vypíše na konci?
#
# >>> KÓD
tajne = 7
tip = int(input("Tip: "))
pokusy = 1
while tip != tajne:                 # != znamená „není rovno“
    tip = int(input("Tip: "))
    pokusy = pokusy + 1
print("Správně na", pokusy, "pokusů")
# <<< KÓD
#
# PROČ: první tip se přečte před cyklem (jinak by podmínka neměla co
# porovnat). Pak se čte znovu a znovu, dokud se netrefí. Počet kol dopředu
# nikdo nezná, proto while a ne for.
#
# ZKUS: přidej do cyklu nápovědu „víc“ / „míň“ (if tip < tajne: …).
