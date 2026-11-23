# d18_ip.py — IP adresa jsou čtyři bajty: text rozsekej, převeď, ulož do seznamu
#
# PŘEDPOVĚĎ: seznam, součet a poslední bajt + 1. Jaké?
#
# >>> KÓD
ip = "192.168.1.10"
casti = ip.split(".")               # text rozsekaný podle tečky: ['192', '168', '1', '10']
bajty = []
for c in casti:
    bajty.append(int(c))            # z textu číslo
print(bajty, sum(bajty), bajty[3] + 1)
# <<< KÓD
#
# PROČ: split vrátí seznam textů; čísla z nich udělá int. IP adresa je
# opravdu jen čtveřice bajtů 0–255 (PRGA-05, bajty z PRGA-09), v paměti
# zabírá 4 bajty, tečky jsou jen pro lidi.
#
# ZKUS: "192.168.1.256". Projde? Přidej kontrolu, že každý bajt je 0–255,
# a vypiš "neplatná", když není.
