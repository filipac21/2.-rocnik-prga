# Síť 5 — propustnost vlastníma rukama
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# nettest.cz nebo speedtest.net nedělají žádnou magii: stáhnou kus dat,
# změří čas a vydělí. Tenhle program to udělá taky, v šesti řádcích.
# Stáhne zkušební soubor o 10 MB z veřejného testovacího serveru,
# stopne dobu a spočítá propustnost v megabitech za sekundu.
#
# Pozor na jednotky, to je celá pointa: soubor měříme v bajtech, síť
# v bitech za sekundu. Bajt má 8 bitů. Proto se násobí osmi.
# Výsledek bude nižší než u nettest.cz: jeden soubor, jedno spojení,
# a první sekundu se spojení teprve rozjíždí.
#
# >>> KÓD — tohle opisuješ
import time
import urllib.request

adresa = "https://proof.ovh.net/files/10Mb.dat"
print("Stahuji", adresa)

zacatek = time.perf_counter()
data = urllib.request.urlopen(adresa, timeout=60).read()
doba = time.perf_counter() - zacatek

bajtu = len(data)
bitu = bajtu * 8
print(f"Staženo {bajtu / 1_000_000:.1f} MB za {doba:.2f} s")
print(f"Propustnost: {bitu / doba / 1_000_000:.1f} Mbit/s")
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# import time  /  import urllib.request
#     Stopky a knihovna, která umí stahovat z webu (urllib = URL library,
#     request = požadavek).
#
# adresa = "https://proof.ovh.net/files/10Mb.dat"
#     Zkušební soubor, který firma OVH nabízí přesně k tomuhle účelu.
#     Náhradní, kdyby nešel: http://speedtest.tele2.net/10MB.zip
#
# zacatek = time.perf_counter()
#     Stopky start.
#
# data = urllib.request.urlopen(adresa, timeout=60).read()
#     Dvě věci v jednom řádku: urlopen otevře spojení a pošle požadavek
#     HTTP, .read() stáhne celý obsah do paměti. Výsledek je hromada
#     bajtů v proměnné data. timeout 60: po minutě bez dat to vzdej.
#
# doba = time.perf_counter() - zacatek
#     Stopky stop, rozdíl v sekundách.
#
# bajtu = len(data)
#     Kolik bajtů jsme stáhli. len() je stejná funkce jako u délky jména
#     v ptaní 1, jen počítá bajty místo písmen.
#
# bitu = bajtu * 8
#     Jeden bajt je osm bitů. Rychlosti sítí se udávají v bitech, proto
#     100 Mbit/s linka stáhne jen 12,5 MB za sekundu. Na tohle se zapomíná
#     nejčastěji.
#
# print(f"Staženo {bajtu / 1_000_000:.1f} MB za {doba:.2f} s")
#     Podtržítka v čísle 1_000_000 Python ignoruje, jsou jen pro čitelnost.
#     Dělením miliónem dostaneme megabajty.
#
# print(f"Propustnost: {bitu / doba / 1_000_000:.1f} Mbit/s")
#     Bity za sekundu, děleno miliónem = megabity za sekundu. Tohle číslo
#     porovnej s tím, co ukázal nettest.cz.
#
# Co si z toho odnést: propustnost je měřená veličina a vždycky vyjde
# jinak podle toho, odkud, kam, kdy a jak měříš. Šířka pásma linky je
# teoretický strop, propustnost je to, co doopravdy dostaneš.
