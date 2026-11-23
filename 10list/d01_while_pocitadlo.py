# d01_while_pocitadlo.py — while: opakuj, dokud platí podmínka
#
# PŘEDPOVĚĎ: co vypíše? Napiš si to na papír, teprve pak spusť.
#
# >>> KÓD
i = 1                      # počítadlo začíná na 1
while i <= 5:              # dokud je i nejvýš 5…
    print(i, end=" ")      # …vypiš ho (end=" " = mezera místo nového řádku)
    i = i + 1              # a zvětši; bez tohoto řádku by cyklus nikdy neskončil
print("konec", i)          # sem se dostaneme, až podmínka přestane platit
# <<< KÓD
#
# PROČ: for projde hotovou řadu (range, seznam). while opakuje, DOKUD platí
# podmínka, a o počítadlo se musíš postarat sám: nastavit před cyklem,
# měnit uvnitř. Po skončení je i rovno 6: to je hodnota, při které podmínka
# poprvé neplatila.
#
# ZKUS: změň 5 na 0. Kolikrát se tělo cyklu provede? Co se vypíše?
