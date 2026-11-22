# Funkce 1 — tabulka hodnot: z každého x spočítej y
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# V tabulkovém procesoru jsi měl sloupec x a vedle něj sloupec y = 2x + 1.
# Vzorec jsi napsal jednou a roztáhl dolů. Python dělá totéž cyklem for:
# vezme první x ze seznamu, spočítá y, vypíše řádek, vezme další x…
# až seznam dojde. Seznam je hranatá závorka s hodnotami oddělenými čárkou.
#
# >>> KÓD — tohle opisuješ
xs = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]   # sloupec x jako seznam

print("    x      y")
for x in xs:                  # pro každé x ze seznamu…
    y = 2 * x + 1             # …spočítej y (tohle je ta funkce)
    print(f"{x:5}  {y:5}")    # …a vypiš jeden řádek tabulky
print("hotovo")               # není odsazené: provede se jednou, až po cyklu
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# xs = [-5, -4, …, 5]
#     Seznam (list): jedenáct čísel v hranatých závorkách, oddělených
#     čárkou. Je to jedna proměnná, která drží víc hodnot najednou. Jméno
#     xs čti „iksy“: hodně x. Zkus: print(len(xs)) vypíše 11,
#     print(xs[0]) vypíše -5 (počítá se od nuly).
#
# for x in xs:
#     Cyklus. Čti: „pro každé x ze seznamu xs udělej, co je odsazené pod
#     tím“. Python si vezme první hodnotu (-5), uloží ji do proměnné x,
#     provede tělo cyklu, pak vezme -4… Dvojtečka na konci je povinná.
#
#     y = 2 * x + 1
#     Tělo cyklu je odsazené čtyřmi mezerami. Tohle je ta funkce: v matice
#     y = 2x + 1, v Pythonu musí být hvězdička. Při prvním průchodu je
#     x = -5, takže y = -9.
#
#     print(f"{x:5}  {y:5}")
#     f-string z října. {x:5} = vypiš x na pět míst (zarovnané doprava),
#     dvě mezery, y na pět míst. Díky tomu jsou sloupce pod sebou.
#
# print("hotovo")
#     Není odsazené, takže do cyklu nepatří. Provede se jednou, až cyklus
#     skončí. Odsazení je v Pythonu jediné, co říká, co je uvnitř cyklu.
#
# Zkus: místo seznamu napiš range(-5, 6). Vypisuje totéž: range dává čísla
# od -5 do 5 (horní mez se nebere). Hodí se, když jdou čísla po jedné.
