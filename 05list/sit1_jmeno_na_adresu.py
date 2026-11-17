# Síť 1 — jméno na adresu (DNS)
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Když napíšeš do prohlížeče www.seznam.cz, počítač to jméno nejdřív
# musí přeložit na číselnou IP adresu, protože sítí putují jen čísla.
# Překlad dělá jmenný systém DNS: celosvětový telefonní seznam serverů.
# Python se ho umí zeptat jedním řádkem.
#
# Program se zeptá na jméno serveru, vypíše jeho IPv4 adresu a pak
# všechny adresy, které DNS vrátí. Velké weby jich mívají víc (rozkládají
# zátěž) a často mají vedle krátké IPv4 adresy (4 čísla) i dlouhou IPv6
# adresu (osm skupin oddělených dvojtečkami).
#
# >>> KÓD — tohle opisuješ
import socket

jmeno = input("Jméno serveru (třeba www.seznam.cz): ")
adresa = socket.gethostbyname(jmeno)
print(jmeno, "má IPv4 adresu", adresa)

vsechny = socket.getaddrinfo(jmeno, 443, proto=socket.IPPROTO_TCP)
print("Všechny adresy, které DNS vrátilo:")
for zaznam in vsechny:
    print("  ", zaznam[4][0])
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# import socket
#     Knihovna socket je v Pythonu základ pro všechno síťové: překlad
#     jmen, navazování spojení, posílání dat. Název znamená „zásuvka“:
#     konec spojení, do kterého se zapojí program.
#
# jmeno = input("Jméno serveru (třeba www.seznam.cz): ")
#     Zeptá se na jméno. Piš bez https:// a bez lomítek, jen jméno.
#
# adresa = socket.gethostbyname(jmeno)
#     Funkce „get host by name“ se zeptá DNS a vrátí jednu IPv4 adresu
#     jako text, třeba "77.75.77.222". Když jméno neexistuje nebo není
#     internet, spadne na socket.gaierror: „name or service not known“.
#
# print(jmeno, "má IPv4 adresu", adresa)
#     Výpis.
#
# vsechny = socket.getaddrinfo(jmeno, 443, proto=socket.IPPROTO_TCP)
#     Důkladnější dotaz: vrať všechno, co o jménu víš, pro port 443
#     (to je HTTPS, zabezpečený web) a protokol TCP. Výsledek je seznam
#     záznamů, každý záznam je n-tice s několika údaji.
#
# for zaznam in vsechny:
#     Cyklus přes záznamy, stejně jako for u kmitání: „pro každý záznam
#     v seznamu udělej odsazené řádky“.
#
#     print("  ", zaznam[4][0])
#     Z každého záznamu vezmeme pátou položku (index 4, počítá se od nuly),
#     to je adresa i s portem, a z ní první část (index 0), samotnou adresu.
#     Hranaté závorky jsou výběr položky ze seznamu, prosinec to probere
#     pořádně.
#
# Co si z toho odnést: DNS překládá jména na adresy. Jedno jméno může
# mít adres víc, a může mít IPv4 (32 bitů) i IPv6 (128 bitů).
