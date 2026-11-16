# b5_negativ.py — negativ: každý bajt pixelu nahraď 255 − bajt
#
# JAK TO FUNGUJE
# --------------
# Barva je číslo 0–255. 255 − číslo ji obrátí: z černé bílá, z bílé černá,
# z červené (0, 0, 255) azurová (255, 255, 0). Stačí jeden cyklus přes
# všechny bajty za hlavičkou, bez rozlišování barev.
#
# Spuštění:  python b5_negativ.py cara_cervena.bmp   → cara_cervena_negativ.bmp
#
# >>> KÓD — tohle opisuješ
import sys

soubor = sys.argv[1] if len(sys.argv) > 1 else input("soubor: ")
data = bytearray(open(soubor, "rb").read())
zacatek = int.from_bytes(data[10:14], "little")

for i in range(zacatek, len(data)):                # každý bajt pixelů, jeden po druhém
    data[i] = 255 - data[i]

novy = soubor.replace(".bmp", "_negativ.bmp")
open(novy, "wb").write(data)
print("uloženo:", novy)
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# range(zacatek, len(data))
#     Krok 1: tentokrát je jedno, který bajt je modrá a který červená,
#     obrací se všechny stejně. Hlavičku (před zacatek) nech být, jinak
#     soubor přestane být BMP.
# 255 - data[i]
#     0 → 255, 255 → 0, 100 → 155. Dvakrát za sebou = původní obrázek.
#
# Zkus: jen jeden kanál: for p in range(zacatek, len(data), 3): data[p + 1] = 0
#       (zelená pryč: z bílé fialová, z černé pořád černá).
# Zkus: ztmavit o polovinu: data[i] = data[i] // 2. Zesvětlit: (data[i] + 255) // 2.
