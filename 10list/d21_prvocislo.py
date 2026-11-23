# d21_prvocislo.py — BONUS: while hledá dělitele; prvočíslo nemá žádný
#
# PŘEDPOVĚĎ: pro 29 a pro 51. Co vypíše?
#
# >>> KÓD
n = int(input("Číslo: "))
d = 2
while d < n and n % d != 0:         # zkoušej dělitele, dokud nějaký nedělí
    d = d + 1
if d == n:
    print(n, "je prvočíslo")
else:
    print(n, "dělí", d)
# <<< KÓD
#
# PROČ: cyklus skončí dvěma způsoby: buď d doběhlo až k n (nic nedělilo →
# prvočíslo), nebo n % d == 0 (našel se dělitel). Po cyklu se podle d pozná,
# který to byl. Pro 51 je to 3 (51 = 3 · 17).
#
# ZKUS: vypiš všechna prvočísla do 50 (cyklus for kolem tohoto while).
