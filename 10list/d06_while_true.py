# d06_while_true.py — while True + break: cyklus bez podmínky v hlavičce
#
# PŘEDPOVĚĎ: jaké bude n a jaký součet?
#
# >>> KÓD
soucet = 0
n = 1
while True:                         # „navždy“: končí jen přes break
    soucet = soucet + n
    if soucet > 20:
        break
    n = n + 1
print("n =", n, "součet =", soucet)
# <<< KÓD
#
# PROČ: 1 + 2 + 3 + 4 + 5 = 15, + 6 = 21 > 20 → break. Součet tedy přeskočil
# dvacítku při n = 6. while True je běžný zápis, když se podmínka konce hodí
# až doprostřed těla.
#
# ZKUS: změň 20 na 100. Pak smaž řádek n = n + 1: program běží dál? Proč
# skončí, i když se n nemění? (Sleduj, co se děje se součtem.)
