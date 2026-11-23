# d12_maximum.py — největší hodnota a KDE je: index přes range(len())
#
# PŘEDPOVĚĎ: co se vypíše?
#
# >>> KÓD
body = [7, 10, 4, 9]
nej = body[0]                       # zatím nejlepší je první
kde = 0
for i in range(len(body)):          # i = 0, 1, 2, 3
    if body[i] > nej:
        nej = body[i]
        kde = i
print(nej, "na indexu", kde)
# <<< KÓD
#
# PROČ: max(body) umí najít hodnotu, ale ne pozici. Když potřebuješ index,
# procházíš indexy (range(len())) a pamatuješ si, kde jsi nejlepší viděl.
#
# ZKUS: najdi nejmenší hodnotu a její index. Pak dej do seznamu dvě desítky:
# kterou najde a proč?
