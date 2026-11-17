# Síť 2 — moje adresa a kdo mě vidí
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Každé zařízení v síti má IP adresu. Tenhle program zjistí, jak se
# jmenuje tvůj počítač a jakou má adresu v místní síti. Pak se na tu
# adresu podívá blíž: je to adresa privátní (platí jen uvnitř školy),
# nebo veřejná (platí v celém internetu)? A ukáže, že IPv4 adresa je
# ve skutečnosti jedno 32bitové číslo, které si lidé pro pohodlí
# zapisují jako čtyři čísla oddělená tečkami.
#
# Pointa přijde, až adresu porovnáš s tím, co ti ukáže nettest.cz:
# tam uvidíš JINOU adresu. Tu veřejnou má školní směrovač a za ní
# schovává všechny počítače ve škole. Říká se tomu NAT.
#
# >>> KÓD — tohle opisuješ
import socket
import ipaddress

pocitac = socket.gethostname()
moje_ip = socket.gethostbyname(pocitac)
print("Tenhle počítač se jmenuje", pocitac, "a má adresu", moje_ip)

adresa = ipaddress.ip_address(moje_ip)
print("Verze protokolu IP:", adresa.version)
print("Je to privátní adresa:", adresa.is_private)
print("Adresa jako jedno číslo:", int(adresa))
print("Adresa binárně:", bin(int(adresa)))
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# import socket  /  import ipaddress
#     Dvě knihovny: socket umí mluvit se sítí, ipaddress umí s adresami
#     počítat (rozebrat je, porovnat, zjistit, do které sítě patří).
#
# pocitac = socket.gethostname()
#     Jméno tohoto počítače, jak ho zná operační systém (třeba UC207-12).
#
# moje_ip = socket.gethostbyname(pocitac)
#     Stejná funkce jako v programu 1, jen se ptáme na vlastní jméno.
#     Vrátí adresu, kterou má tvůj počítač v místní síti. Když má počítač
#     víc síťových karet (kabel, Wi-Fi, virtuální), může vrátit jinou,
#     než čekáš. To není chyba, jen má víc adres.
#
# adresa = ipaddress.ip_address(moje_ip)
#     Z textu "10.0.5.23" udělá objekt adresy, se kterým se dá pracovat.
#
# print("Verze protokolu IP:", adresa.version)
#     4, nebo 6.
#
# print("Je to privátní adresa:", adresa.is_private)
#     True pro rozsahy 10.x.x.x, 172.16–31.x.x a 192.168.x.x (a pár
#     dalších). Privátní adresy se smí libovolně opakovat v různých
#     sítích po světě, protože ven z místní sítě se nedostanou. Ve škole
#     vyjde skoro jistě True.
#
# print("Adresa jako jedno číslo:", int(adresa))
#     IPv4 adresa je 32 bitů, tedy číslo od 0 do 4 294 967 295. Čtyři
#     čísla s tečkami jsou jen zápis pro lidi, každé je jeden bajt.
#
# print("Adresa binárně:", bin(int(adresa)))
#     Totéž číslo ve dvojkové soustavě, uvidíš až 32 jedniček a nul.
#     Příští program s těmi bity bude pracovat: prvních N z nich říká,
#     do které sítě adresa patří.
#
# Co si z toho odnést: tvůj počítač má privátní adresu, internet vidí
# veřejnou adresu školního směrovače. Překladu mezi nimi se říká NAT
# a je to důvod, proč se na tvůj počítač z internetu nikdo přímo
# nedovolá. IP adresa je 32bitové číslo.
