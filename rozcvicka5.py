import math

for i in range(10):
    print(i, math.sin(i))

print("--- a teď jako pozice ---")

for i in range(30):
    cislo = math.sin(i * 0.25)
    pozice = int(10 + 10 * cislo)
    print(" " * pozice + "O")