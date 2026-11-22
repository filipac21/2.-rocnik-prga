# Funkce 4 — sigmoid, ReLU a práh: první if
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Sigmoid je vzorec. ReLU a práh vzorcem nejsou: rozhodují se podle toho,
# jestli je x záporné. Na to je příkaz if: „když platí podmínka, udělej
# tohle, jinak (else) tamto“. Podmínka je porovnání z října (x < 0),
# které vrací True nebo False.
#
# >>> KÓD — tohle opisuješ
import math

print("    x    sigmoid   ReLU   práh")
for x in range(-5, 6):
    sigmoid = 1 / (1 + math.exp(-x))   # vždy mezi 0 a 1, v nule 0,5

    if x < 0:            # ReLU: záporné usekne na nulu…
        relu = 0
    else:                # …kladné (a nulu) pustí beze změny
        relu = x

    if x > 0:            # práh: buď 1, nebo 0, nic mezi
        prah = 1
    else:
        prah = 0

    print(f"{x:5}  {sigmoid:8.3f}  {relu:5}  {prah:5}")
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# math.exp(-x)
#     e na mínus x (e = 2,718…). Pro velké kladné x je to skoro nula,
#     takže sigmoid je skoro 1. Pro velké záporné x je to obrovské číslo,
#     sigmoid skoro 0. V nule je exp(0) = 1, takže 1 / (1 + 1) = 0,5.
#
# if x < 0:
#     Podmínka a dvojtečka. Pod tím odsazené tělo, které se provede jen
#     když je podmínka True. Při x = -3 ano: relu = 0.
#
# else:
#     „Jinak“: tělo pro případ, že podmínka neplatila. Při x = 3:
#     relu = 3. Při x = 0: podmínka 0 < 0 neplatí, jde se do else,
#     relu = 0. Vyjde stejně, ale jinou cestou. else nemá podmínku,
#     bere všechno ostatní.
#
# if x > 0: prah = 1
#     Práh (skok): ano/ne. Nula tu není kladná, takže práh pro x = 0 dá 0.
#     Hranice je věc rozhodnutí: zkus x >= 0 a sleduj řádek s nulou.
#
# {sigmoid:8.3f}
#     Osm míst, tři desetinná. ReLU a práh jsou celá čísla: {relu:5}.
#
# Zkratka: ReLU se dá napsat jedním řádkem: relu = max(0, x). Dělá totéž.
# Zkus: práh, který přepíná až při x > 2. Které řádky se změní?
# Zkus: tři větve: if x < 0: print("záporné") / elif x == 0: print("nula")
# / else: print("kladné"). elif = „jinak když“. Projde vždy jen jedna.
