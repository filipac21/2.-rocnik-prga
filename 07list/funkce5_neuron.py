# Funkce 5 — neuron je funkce: y = sigmoid(w · x + b)
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Jeden neuron umělé neuronové sítě dělá dvě věci: vynásobí vstup váhou w,
# přičte posun b (to je z = w·x + b, přímka z programu 2) a výsledek
# prožene sigmoidem (program 4), takže ven leze číslo mezi 0 a 1. Víc
# to není. Síť jsou tisíce takových neuronů, kde výstup jednoho je
# vstupem dalších. Učení sítě = počítač sám hledá w a b. To si zkusíme
# v zimě; dnes w a b zadáváš ty a sleduješ, co s křivkou dělají.
#
# >>> KÓD — tohle opisuješ
import math

w = float(input("váha w (zkus 1, 2, -1, 0): "))
b = float(input("posun b (zkus 0, 2, -4): "))

print(f"\nneuron: y = sigmoid(w * x + b)   w = {w}, b = {b}")
print("    x        z        y   graf")
for x in range(-5, 6):
    z = w * x + b                   # vážený součet (zatím jediný vstup)
    y = 1 / (1 + math.exp(-z))      # aktivace: sigmoid stlačí z mezi 0 a 1
    print(f"{x:5}  {z:7.1f}  {y:7.3f}   " + "#" * round(40 * y))
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# z = w * x + b
#     Přímka s parametry z programu 2, jen se jinak jmenují: w jako
#     weight (váha), b jako bias (posun). Říká se tomu vážený součet:
#     u více vstupů by to bylo w1*x1 + w2*x2 + … + b.
#
# y = 1 / (1 + math.exp(-z))
#     Sigmoid z programu 4, ale ne z x, nýbrž ze z. To je celý trik:
#     nejdřív přímka, pak S-křivka. Výsledek 0 až 1 se dá číst jako
#     „jak moc ano“.
#
# "#" * round(40 * y)
#     Graf v terminálu z programu 3: y je nejvýš 1, takže 40 * y je
#     nejvýš 40 mřížek. round, protože mřížek musí být celý počet.
#
# Co sledovat:
#   w = 1, b = 0   → S-křivka s 0,5 v nule (čistý sigmoid)
#   w = 2          → strmější: z roste dvakrát rychleji
#   w = -1         → klesá: velké x dá malé y
#   w = 0          → y je pořád 0,5: na x nezáleží, neuron je „vypnutý“
#   b = 2          → posun doleva: y = 0,5 tam, kde z = 0, tedy x = -b/w = -2
#   w = 2, b = -4  → 0,5 je v x = 2
#
# Zkus: dva vstupy x1, x2 ∈ {0, 1}, w1 = w2 = 10, b = -15: čtyři řádky.
# Neuron se chová jako AND (1 jen když jsou oba vstupy 1). Říjnové and
# v jednom vzorci.
