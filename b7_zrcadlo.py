# b7_zrcadlo.py — zrcadlo: pixel x jde na místo (šířka − 1 − x); pak to zkus na síť z minula
#
# JAK TO FUNGUJE
# --------------
# Zrcadlení zleva doprava: v každém řádku se pixel z pozice x zkopíruje na
# pozici sirka − 1 − x. Kopíruje se z původních bajtů do nové kopie, aby se
# levá půlka nepřepsala dřív, než se přečte.
#
# Spuštění:  python b7_zrcadlo.py trojka.bmp        → trojka_zrcadlo.bmp
# Pak:       python poznej.py trojka_zrcadlo.bmp    (ve složce z PRGA-08 s vahy.txt)
#
# >>> KÓD — tohle opisuješ
import sys

soubor = sys.argv[1] if len(sys.argv) > 1 else input("soubor: ")
data = open(soubor, "rb").read()                   # původní (jen čtení)
nova = bytearray(data)                             # kopie, do které kreslíme
zacatek = int.from_bytes(data[10:14], "little")
sirka = int.from_bytes(data[18:22], "little")
vyska = int.from_bytes(data[22:26], "little")
radek = (sirka * 3 + 3) // 4 * 4

for y in range(vyska):                             # každý řádek (odspodu, je to jedno)
    for x in range(sirka):                         # každý pixel v řádku
        odkud = zacatek + y * radek + x * 3
        kam = zacatek + y * radek + (sirka - 1 - x) * 3
        nova[kam] = data[odkud]                    # modrá
        nova[kam + 1] = data[odkud + 1]            # zelená
        nova[kam + 2] = data[odkud + 2]            # červená

novy = soubor.replace(".bmp", "_zrcadlo.bmp")
open(novy, "wb").write(nova)
print("uloženo:", novy)
# <<< KÓD
#
# VYSVĚTLENÍ
# ----------
# data (bytes) a nova (bytearray)
#     Čteme z data, píšeme do nova. Kdybychom psali do téhož, pixel x = 0
#     by přepsal pixel 239, a když cyklus dojde k x = 239, zkopíruje už
#     přepsanou hodnotu zpátky: výsledek by byl levá půlka dvakrát.
# (sirka - 1 - x)
#     x = 0 → 239, x = 1 → 238, …, x = 239 → 0. Stejný trik jako
#     (vyska - 1 - y) v b3, jen vodorovně.
# y jde přes řádky v souboru
#     Zrcadlíme vodorovně, takže je jedno, jestli řádek 0 je nahoře nebo
#     dole. Pro překlopení SVISLE by se naopak měnilo y a nechávalo x.
#
# Zkus: překlop svisle: odkud = zacatek + y * radek + x * 3,
#       kam = zacatek + (vyska - 1 - y) * radek + x * 3.
# Zkus: pusť na trojka_zrcadlo.bmp poznej.py z PRGA-08: síť naučená na trojky „zleva
#       shora“ tipne 5 nebo 1 (minulý týden část 7). Teď už víš, jak taková kostka vzniká.
