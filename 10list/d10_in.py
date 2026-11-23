# d10_in.py — in: je hodnota v seznamu?
#
# PŘEDPOVĚĎ: uživatel napíše admin. Co se vypíše?
#
# >>> KÓD
zakazane = ["heslo", "1234", "admin"]
heslo = input("Heslo: ")
if heslo in zakazane:
    print("Tohle ne.")
else:
    print("OK, délka", len(heslo))
# <<< KÓD
#
# PROČ: in vrátí True, když se hodnota v seznamu najde, jinak False. Je to
# totéž, co cyklus s porovnáváním a break, jen na jeden řádek. len funguje
# i na text: počet znaků.
#
# ZKUS: zadej Admin s velkým A. Prošlo? Jak porovnat bez ohledu na
# velikost písmen? (heslo.lower())
