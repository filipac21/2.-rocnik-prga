import sys

if len(sys.argv) > 1:
    soubor = sys.argv[1]
else:
    soubor = input("soubor (např. cara.bmp): ")

data = open(soubor, "rb").read()           # bajty, ne text
print("bajtů v souboru:", len(data))

for i in range(16):                        # prvních šestnáct bajtů, každý na řádek
    print(i, data[i])

print("první dva jako text:", data[:2])    # b'BM' = Bitmap
sirka = data[18] + data[19] * 256          # číslo ze dvou bajtů: nižší + vyšší × 256
vyska = data[22] + data[23] * 256
print("šířka:", sirka, " výška:", vyska)
print("totéž hotovou funkcí:", int.from_bytes(data[18:22], "little"))

nul = 0
bilych = 0
for b in data:                             # projde všech 172 854 čísel
    if b == 0:
        nul = nul + 1
    if b == 255:
        bilych = bilych + 1
print("bajtů 0 (černá):", nul, "  bajtů 255 (bílá):", bilych)
print("černých pixelů asi:", nul // 3, "  (tři bajty na pixel)")