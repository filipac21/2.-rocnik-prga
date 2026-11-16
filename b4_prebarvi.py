# b4_prebarvi.py — přebarvi čáru: každý tmavý pixel na červený a ulož nový soubor
#
# JAK TO FUNGUJE
# --------------
# bytes měnit nejde, bytearray ano. Program projde pixely po třech bajtech
# (krok 3), tmavý pixel přepíše na červený (modrá 0, zelená 0, červená 255)
# a výsledek zapíše do nového souboru. Hlavička se nemění, kopíruje se celá.
#
# Spuštění:  python b4_prebarvi.py cara.bmp        → vznikne cara_cervena.bmp
#
# >>> KÓD — tohle opisuješ
import sys

soubor = sys.argv[1] if len(sys.argv) > 1 else input("soubor: ")
data = bytearray(open(soubor, "rb").read())        # bytearray = bajty, které jdou měnit
zacatek = int.from_bytes(data[10:14], "little")

zmeneno = 0
for p in range(zacatek, len(data), 3):             # p = začátek každého pixelu (po třech)
    modra, zelena, cervena = data[p], data[p + 1], data[p + 2]
    if modra < 128 and zelena < 128 and cervena < 128:   # tmavý pixel
        data[p] = 0                                # modrá
        data[p + 1] = 0                            # zelená
        data[p + 2] = 255                          # červená
        zmeneno = zmeneno + 1

novy = soubor.replace(".bmp", "_cervena.bmp")
open(novy, "wb").write(data)                       # wb = zapiš bajty
print("přebarveno pixelů:", zmeneno, "  uloženo:", novy)
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# bytearray(…)
#     Kopie bajtů, do které jde psát: data[p] = 0. Obyčejné bytes by
#     hlásily TypeError: 'bytes' object does not support item assignment.
# range(zacatek, len(data), 3)
#     Od prvního pixelu do konce souboru po třech: p ukazuje vždy na modrý
#     bajt pixelu, p + 1 zelený, p + 2 červený. (U šířky 240 nemá řádek žádnou
#     výplň, takže pixely jdou v souboru souvisle. U jiné šířky by se šlo po
#     řádcích jako v b3.)
# < 128
#     Čára z Malování má okraje šedé (vyhlazení). Hranice 128 vezme vše,
#     co je spíš tmavé. Zkus 50 a uvidíš, že okraje zůstanou šedé.
# open(novy, "wb").write(data)
#     Zapíše všechny bajty včetně hlavičky. Otevři nový soubor poklepáním:
#     Malování / Fotky ho ukážou s červenou čárou.
#
# Zkus: modrá čára (255, 0, 0), zelená (0, 255, 0), žlutá (0, 255, 255): BMP je
#       modrá-zelená-červená, ne RGB.
# Zkus: přebarvi naopak BÍLÉ pozadí (všechny tři ≥ 200) na světle modrou (255, 230, 200).
