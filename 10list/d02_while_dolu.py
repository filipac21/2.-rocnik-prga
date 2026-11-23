# d02_while_dolu.py — while počítá dolů; podmínka se vyhodnocuje před každým kolem
#
# PŘEDPOVĚĎ: kolik řádků se vypíše a jaké číslo bude poslední?
#
# >>> KÓD
n = 50
while n > 0:
    print(n)
    n = n - 20
print("pod nulou:", n)
# <<< KÓD
#
# PROČ: 50 → vypiš, odečti → 30 → vypiš → 10 → vypiš → −10: podmínka n > 0
# neplatí, cyklus končí. Číslo −10 se už nevypíše, ale v proměnné zůstane.
#
# ZKUS: změň 20 na 25. A pak zkus n = n + 20 místo odečítání: co se stane
# a jak program zastavíš? (Ctrl+C v terminálu.)
