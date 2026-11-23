# d17_vstup_do_seznamu.py — while čte hodnoty do seznamu, dokud nepřijde prázdný řádek
#
# PŘEDPOVĚĎ: uživatel napíše 12, 15, 9 a pak jen Enter. Co se vypíše?
#
# >>> KÓD
teploty = []
t = input("Teplota (prázdné = konec): ")
while t != "":
    teploty.append(float(t))
    t = input("Teplota (prázdné = konec): ")
print(len(teploty), "hodnot, průměr", sum(teploty) / len(teploty))
# <<< KÓD
#
# PROČ: tohle je nejčastější tvar „načti, dokud…“: jedno čtení před
# cyklem, jedno na konci těla. Prázdný text "" je znamení konce. float
# převede text na desetinné číslo, append ho uloží.
#
# ZKUS: hned první řádek nech prázdný. Jaká chyba a na kterém řádku?
# Oprav podmínkou.
