# d15_hledej_while.py — while hledá v seznamu: dvě podmínky spojené and
#
# PŘEDPOVĚĎ: na jakém indexu se zastaví a jakou hodnotu vypíše?
#
# >>> KÓD
cisla = [5, 12, 8, 20, 3]
i = 0
while i < len(cisla) and cisla[i] < 15:
    i = i + 1
print("index", i, "hodnota", cisla[i])
# <<< KÓD
#
# PROČ: cyklus posouvá i, dokud je hodnota malá. První podmínka i < len
# hlídá, ať nevyběhneme za konec seznamu; díky and se druhá část ani
# nevyhodnotí, když první neplatí (jinak by cisla[5] spadlo).
#
# ZKUS: změň 15 na 50 (nic tak velkého tam není). Co se stane na posledním
# řádku a proč? Oprav program podmínkou if i < len(cisla).
