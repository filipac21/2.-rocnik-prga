# Síť 6 — co říká server (HTTP), pro rychlíky
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Když prohlížeč žádá stránku, server neposílá jen HTML. Napřed pošle
# stavový kód (200 = v pořádku, 404 = nenalezeno) a hlavičky: kdo jsem,
# jaký typ obsahu posílám, jak je velký. Prohlížeč to před tebou skrývá,
# v nástrojích vývojáře (F12 → Network) je to vidět. Python to umí
# přečíst přímo. Zkus svou vlastní stránku na github.io.
#
# >>> KÓD — tohle opisuješ
import urllib.request

adresa = input("Adresa webu i s https:// : ")
odpoved = urllib.request.urlopen(adresa, timeout=10)

print("Stavový kód:", odpoved.status)
print("Server:     ", odpoved.headers.get("Server"))
print("Typ obsahu: ", odpoved.headers.get("Content-Type"))
obsah = odpoved.read()
print("Velikost:   ", len(obsah), "bajtů")
print("Začátek:    ", obsah[:80])
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# adresa = input("Adresa webu i s https:// : ")
#     Tentokrát celá adresa včetně https://, protože posíláme požadavek
#     HTTP, ne jen dotaz na jméno.
#
# odpoved = urllib.request.urlopen(adresa, timeout=10)
#     Pošle požadavek a vrátí objekt odpovědi. Když server vrátí chybu
#     (404, 403), Python to vyhodí jako HTTPError s tím číslem v hlášce.
#     Zkus schválně neexistující stránku a přečti si ji.
#
# print("Stavový kód:", odpoved.status)
#     200 znamená OK. Další potkáš: 301 přesměrováno, 404 nenalezeno,
#     500 chyba serveru.
#
# print("Server:     ", odpoved.headers.get("Server"))
#     Hlavička Server: jaký program na druhé straně běží (GitHub.com,
#     nginx, cloudflare…). Někdy ji server schválně neposílá, pak None.
#
# print("Typ obsahu: ", odpoved.headers.get("Content-Type"))
#     text/html pro stránku, image/png pro obrázek, application/json pro
#     data. Podle tohohle prohlížeč ví, co s obsahem dělat.
#
# obsah = odpoved.read()
#     Stáhne tělo odpovědi, u stránky je to HTML.
#
# print("Velikost:   ", len(obsah), "bajtů")
#     Kolik bajtů stránka má.
#
# print("Začátek:    ", obsah[:80])
#     Prvních 80 bajtů. Uvidíš b'<!DOCTYPE html>...', písmeno b říká,
#     že jsou to surové bajty, ne text. Hranaté závorky s dvojtečkou jsou
#     výřez, prosinec.
#
# Co si z toho odnést: HTTP je rozhovor otázka–odpověď. Odpověď má
# stavový kód, hlavičky a tělo. Prohlížeč, Python i nettest.cz dělají
# na síti totéž, jen to různě ukazují.
