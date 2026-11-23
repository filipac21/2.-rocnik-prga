# d16_pocitadla.py — seznam počítadel: kolikrát která známka
#
# PŘEDPOVĚĎ: jaký seznam pěti čísel se vypíše?
#
# >>> KÓD
znamky = [1, 2, 1, 3, 5, 2, 1, 4]
pocty = [0] * 6                     # šest nul: index 0 nepoužijeme, 1–5 známky
for z in znamky:
    pocty[z] = pocty[z] + 1         # známka je rovnou index do počítadel
print(pocty[1:])
# <<< KÓD
#
# PROČ: místo pěti proměnných jedniček, dvojek… je jeden seznam a hodnota
# známky říká, které počítadlo zvětšit. Stejný trik dělaly pruhy b8 v
# PRGA-09 (index = x // 30).
#
# ZKUS: přidej známku 6. Jaká chyba? Jak by měl být dlouhý seznam pocty?
