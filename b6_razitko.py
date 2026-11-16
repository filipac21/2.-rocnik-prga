# b6_razitko.py — vodoznak: tvůj vzor 8×8 vyražený do rohu obrázku, každé políčko 6×6 pixelů
#
# JAK TO FUNGUJE
# --------------
# Vzor je seznam osmi textů po osmi znacích (# = barva, . = nic), stejně
# jako kostky.txt z minula. Program ho projde řádek po řádku, znak po
# znaku, a každé # nakreslí jako čtvereček k × k pixelů do pravého dolního
# rohu. Adresa pixelu je stejná jako v b3.
#
# Spuštění:  python b6_razitko.py cara.bmp          → cara_razitko.bmp
#
# >>> KÓD — tohle opisuješ
import sys

vzor = [                     # přepiš na svoje iniciály nebo značku
    "#....#..",
    "#....#..",
    "#....#..",
    "#....#..",
    "#....#..",
    "#....#..",
    "#....##.",
    ".####..#",
]
k = 6                        # velikost jednoho políčka v pixelech
barva = (0, 0, 255)          # modrá, zelená, červená → červená

soubor = sys.argv[1] if len(sys.argv) > 1 else input("soubor: ")
data = bytearray(open(soubor, "rb").read())
zacatek = int.from_bytes(data[10:14], "little")
sirka = int.from_bytes(data[18:22], "little")
vyska = int.from_bytes(data[22:26], "little")
radek = (sirka * 3 + 3) // 4 * 4

x0 = sirka - 8 * k - 20      # levý horní roh razítka: 20 px od pravého okraje
y0 = vyska - 8 * k - 20      # a 20 px od spodního

nakresleno = 0
for r in range(8):                       # řádek vzoru
    for s in range(8):                   # sloupec vzoru
        if vzor[r][s] == "#":            # vzor[r] je text, vzor[r][s] jeden znak
            for dy in range(k):          # políčko k × k pixelů
                for dx in range(k):
                    x = x0 + s * k + dx
                    y = y0 + r * k + dy
                    pozice = zacatek + (vyska - 1 - y) * radek + x * 3
                    data[pozice] = barva[0]
                    data[pozice + 1] = barva[1]
                    data[pozice + 2] = barva[2]
                    nakresleno = nakresleno + 1

novy = soubor.replace(".bmp", "_razitko.bmp")
open(novy, "wb").write(data)
print("nakresleno pixelů:", nakresleno, "  uloženo:", novy)
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# vzor[r][s]
#     vzor je seznam textů, vzor[r] je r-tý text (řádek), vzor[r][s] je
#     s-tý znak toho textu. Dva indexy = tabulka. Stejně bude vypadat
#     seznam seznamů v prosinci.
# čtyři cykly v sobě
#     r a s procházejí 64 políček vzoru; dy a dx 36 pixelů každého
#     políčka s #. Dohromady 64 · 36 = 2 304 průchodů nejvnitřnějšího
#     těla, kdyby byl vzor plný; u téhle značky 17 · 36 = 612.
# x0, y0
#     Roh razítka spočítaný ze šířky a výšky, takže funguje i na jinak
#     velkém obrázku. Levý horní roh: x0 = 20, y0 = 20.
#
# Zkus: k = 10 (větší razítko), barva (255, 0, 0) (modrá), jiný roh.
# Zkus: místo pevné barvy pixel ztmav: data[pozice] = data[pozice] // 2 (průhledný vodoznak).
# Zkus: vzor načti ze souboru: vzor = open("vzor.txt").read().split() (8 řádků bez mezer).
