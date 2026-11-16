# b8_sloupce.py — kolik je tmavých pixelů v každém z osmi svislých pruhů: seznam počtů a graf
#
# JAK TO FUNGUJE
# --------------
# Obrázek rozdělíme na 8 svislých pruhů po 30 pixelech. Pro každý pruh
# spočítáme tmavé pixely do seznamu pocty (8 čísel). To je přesně princip
# mřížky 8×8 z PRGA-08, jen v jednom rozměru: z 57 600 pixelů 8 čísel.
#
# Spuštění:  python b8_sloupce.py trojka.bmp
#
# >>> KÓD — tohle opisuješ
import sys

soubor = sys.argv[1] if len(sys.argv) > 1 else input("soubor: ")
data = open(soubor, "rb").read()
zacatek = int.from_bytes(data[10:14], "little")
sirka = int.from_bytes(data[18:22], "little")
vyska = int.from_bytes(data[22:26], "little")
radek = (sirka * 3 + 3) // 4 * 4

pocty = [0] * 8                                    # osm nul: [0, 0, 0, 0, 0, 0, 0, 0]
sirka_pruhu = sirka // 8                           # 30

for y in range(vyska):
    for x in range(sirka):
        pozice = zacatek + y * radek + x * 3
        if data[pozice] < 128:                     # tmavý pixel
            pruh = x // sirka_pruhu                # 0–29 → 0, 30–59 → 1, …
            pocty[pruh] = pocty[pruh] + 1          # přičti do správného pruhu

print("tmavých pixelů v pruzích:", pocty)
print("celkem:", sum(pocty), "  nejplnější pruh:", pocty.index(max(pocty)))
for i in range(8):
    print(i, f"{pocty[i]:5d}", "#" * (pocty[i] // 50))   # jeden # za 50 pixelů
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# [0] * 8
#     Seznam osmi nul. pocty[pruh] = pocty[pruh] + 1 zvedne počítadlo
#     jen v tom pruhu, kam pixel patří. Osm počítadel v jednom seznamu
#     místo osmi proměnných: to je důvod, proč seznamy existují.
# x // sirka_pruhu
#     Celočíselné dělení: 0..29 dá 0, 30..59 dá 1, … 210..239 dá 7. Z
#     pozice pixelu číslo pruhu jedním výrazem, bez osmi if.
# pocty.index(max(pocty))
#     index = na kterém místě v seznamu je hodnota. Pruh s nejvíc inkoustem.
# f"{pocty[i]:5d}"
#     Číslo zarovnané na 5 míst, ať graf nelítá.
#
# Zkus: vodorovné pruhy (y // sirka_pruhu). Pak obojí najednou: pocty[radek_pruhu][sloupec_pruhu]
#       je seznam osmi seznamů po osmi, a máš mřížku 8×8 z PRGA-08 napsanou sám.
# Zkus: ohraničení kostky: nejmenší a největší x, kde je tmavý pixel (min_x = sirka na začátku,
#       if x < min_x: min_x = x). Přesně to dělá obrazek.py, než mřížku spočítá.
