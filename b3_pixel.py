# b3_pixel.py — adresa pixelu: kde v souboru leží pixel (x, y), a náhled 8×8 z pixelů
#
# JAK TO FUNGUJE
# --------------
# Pixely začínají za hlavičkou (bajt 54) a jdou po řádcích ODSPODU, každý
# pixel = 3 bajty (modrá, zelená, červená). Řádek má šířka × 3 bajtů,
# zaokrouhleno nahoru na násobek 4 (u 240 px je to přesně 720).
# Pixel (x, y), kde y počítáme shora jako v Malování, leží na adrese
#     zacatek + (vyska − 1 − y) · radek + x · 3
# Program vypíše barvu jednoho pixelu a pak každý třicátý pixel: náhled 8×8.
#
# Spuštění:  python b3_pixel.py trojka.bmp
#
# >>> KÓD — tohle opisuješ
import sys

soubor = sys.argv[1] if len(sys.argv) > 1 else input("soubor: ")
data = open(soubor, "rb").read()

zacatek = int.from_bytes(data[10:14], "little")    # kde začínají pixely (54)
sirka = int.from_bytes(data[18:22], "little")
vyska = int.from_bytes(data[22:26], "little")
radek = (sirka * 3 + 3) // 4 * 4                   # bajtů na jeden řádek (720)
print(f"{sirka} × {vyska}, pixely od {zacatek}, řádek {radek} bajtů")

x = int(input("x (0–239): "))
y = int(input("y shora (0–239): "))
pozice = zacatek + (vyska - 1 - y) * radek + x * 3
print("pixel leží na bajtech", pozice, "až", pozice + 2)
print("modrá, zelená, červená:", data[pozice], data[pozice + 1], data[pozice + 2])

print("\nnáhled (každý 30. pixel, # = tmavý):")
for y in range(0, vyska, 30):                      # 0, 30, 60, … 210: osm řádků
    for x in range(0, sirka, 30):                  # osm sloupců
        pozice = zacatek + (vyska - 1 - y) * radek + x * 3
        if data[pozice] < 128:                     # stačí modrá: černá má 0, bílá 255
            print("#", end="")                     # end="" = bez nového řádku
        else:
            print(".", end="")
    print()                                        # konec řádku náhledu
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# (vyska - 1 - y)
#     Soubor má spodní řádek první. Řádek y = 0 (nahoře) je v souboru
#     poslední, tedy řádek číslo 239. Proto se odečítá.
# x * 3
#     Každý pixel má tři bajty, pixel x začíná o 3·x dál než začátek řádku.
# range(0, vyska, 30)
#     Třetí číslo je krok: 0, 30, 60, … Osm hodnot = osm řádků náhledu.
#     Cyklus v cyklu: vnější řádky, vnitřní sloupce. Vnitřní proběhne celý
#     pro každý jeden průchod vnějšího (8 × 8 = 64 pixelů).
# print("#", end="")
#     Normálně print skočí na nový řádek; end="" to vypne. Prázdný print()
#     pak řádek ukončí.
#
# Zkus: krok 10 místo 30 → náhled 24×24. Krok 5 → 48×48 (už vypadá jako obrázek).
# Zkus: místo data[pozice] < 128 použij data[pozice + 2] (červený kanál). Na černobílém
#       obrázku je to stejné; na přebarveném z b4 už ne.
