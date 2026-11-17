# Síť 7 — jedna adresa, mnoho webů (pro rychlíky)
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Z programu 1 víš, že github.io má čtyři IP adresy. Na nich ale neběží
# jeden web, běží jich tam statisíce, včetně toho tvého. Jak server
# pozná, který chceš? Prohlížeč mu jméno webu pošle v požadavku,
# v hlavičce Host. Když zadáš do prohlížeče jen holou IP adresu, žádné
# jméno nepošleš a server neví, co ti dát: vrátí chybu 404.
#
# Program pošle na JEDNU a tu samou adresu tři požadavky, pokaždé
# s jiným jménem v hlavičce Host, a vypíše, co server odpověděl.
# Třetí pokus si uprav na svůj web: jméno tvojejmeno.github.io
# a cesta /nazev-tveho-repozitare/.
#
# >>> KÓD — tohle opisuješ
import http.client

adresa_ip = "185.199.108.153"
pokusy = [
    ("185.199.108.153", "/"),
    ("pages.github.com", "/"),
    ("tvojejmeno.github.io", "/nazev-webu/"),
]

for jmeno, cesta in pokusy:
    spojeni = http.client.HTTPConnection(adresa_ip, timeout=10)
    spojeni.request("GET", cesta, headers={"Host": jmeno})
    odpoved = spojeni.getresponse()
    print(f"{jmeno:<24} {odpoved.status} {odpoved.reason}")
    print("    Location:", odpoved.getheader("Location"))
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# import http.client
#     Nižší patro než urllib z programu 6: tady si požadavek HTTP
#     skládáme sami a vidíme každou hlavičku. Přesně to, co dělá
#     prohlížeč pod kapotou.
#
# adresa_ip = "185.199.108.153"
#     Jedna ze čtyř adres GitHub Pages. Všechny tři požadavky půjdou sem.
#
# pokusy = [ (jméno, cesta), (jméno, cesta), (jméno, cesta) ]
#     Seznam dvojic. První dvojice posílá jako „jméno“ samotnou adresu,
#     to je totéž, jako když do prohlížeče napíšeš holou IP. Druhá je
#     veřejný web GitHubu. Třetí si přepiš na svůj web.
#
# for jmeno, cesta in pokusy:
#     Cyklus přes dvojice: v každém průchodu se první část dvojice uloží
#     do jmeno a druhá do cesta. Prosinec, kolekce.
#
#     spojeni = http.client.HTTPConnection(adresa_ip, timeout=10)
#     Připrav spojení na adresu (port 80, obyčejné HTTP, ať vidíme
#     odpověď bez šifrování).
#
#     spojeni.request("GET", cesta, headers={"Host": jmeno})
#     Pošli požadavek: metoda GET, cesta, a v hlavičce Host jméno webu.
#     Tohle je ten jediný řádek, kterým se tři pokusy liší.
#
#     odpoved = spojeni.getresponse()
#     Přečti odpověď serveru: stavový kód, text a hlavičky.
#
#     print(f"{jmeno:<24} {odpoved.status} {odpoved.reason}")
#     Jméno zarovnané vlevo, kód a slovní popis: 404 Not Found,
#     301 Moved Permanently.
#
#     print("    Location:", odpoved.getheader("Location"))
#     Při 301 server říká „jdi sem“: na https:// verzi téhož webu. Tam ti
#     prohlížeč jde automaticky, proto přesměrování normálně nevidíš.
#     U 404 je Location None, žádné „sem“ není.
#
# Co si z toho odnést: IP adresa říká, ke kterému počítači jít. Který
# web na něm chceš, říká jméno v hlavičce Host (a u HTTPS už při
# navazování šifrování). Proto holá IP adresa v prohlížeči web neukáže.
# DNS tedy pro web funguje jen jedním směrem: ze jména na adresu.
