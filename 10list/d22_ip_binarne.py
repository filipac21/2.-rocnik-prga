# d22_ip_binarne.py — BONUS: každý bajt IP adresy na osm bitů (d07 + d18)
#
# PŘEDPOVĚĎ: čtyři řádky, na každém číslo a osm bitů. Jaké pro 192?
#
# >>> KÓD
ip = "192.168.1.10"
for c in ip.split("."):
    n = int(c)
    bity = ""
    while len(bity) < 8:            # vždy osm číslic, i s nulami vlevo
        bity = str(n % 2) + bity
        n = n // 2
    print(c, bity)
# <<< KÓD
#
# PROČ: oproti d07 cyklus neběží „dokud n > 0“, ale „dokud nemám 8 bitů“:
# u 1 tak vzniknou nuly vlevo (00000001). Tohle je zápis, který uvidíš u
# masky sítě: /24 = 11111111.11111111.11111111.00000000.
#
# ZKUS: vypiš masku pro /24 a pro /20 (kolik jedniček, kolik nul).
