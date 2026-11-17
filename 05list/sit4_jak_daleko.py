# Síť 4 — jak daleko je server (zpoždění)
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# Druhý základní parametr sítě vedle rychlosti je zpoždění: jak dlouho
# trvá, než se signál dostane k serveru a zpátky. Program to změří tak,
# že k několika serverům naváže spojení na port 443 (to je HTTPS, web)
# a stopne, jak dlouho navázání trvalo. Navázání spojení je přesně
# jedna cesta tam a zpátky, takže výsledek je zpoždění v milisekundách.
#
# Servery jsou seřazené od Prahy po Austrálii. Sleduj, jak čísla rostou.
# Světlo v optickém vlákně letí asi 200 000 km za sekundu, a to je
# strop, který žádná technika neobejde.
#
# >>> KÓD — tohle opisuješ
import socket
import time

servery = ["www.seznam.cz", "www.vut.cz", "www.google.com", "www.nic.br", "www.gov.au"]

for server in servery:
    zacatek = time.perf_counter()
    spojeni = socket.create_connection((server, 443), timeout=5)
    konec = time.perf_counter()
    spojeni.close()
    ms = (konec - zacatek) * 1000
    print(f"{server:<16} {ms:7.1f} ms")
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# import socket  /  import time
#     Síť a stopky.
#
# servery = ["www.seznam.cz", ...]
#     Seznam jmen v hranatých závorkách. Seznamy probereme v prosinci,
#     dnes stačí: je to víc hodnot pohromadě a for je projde po jedné.
#     Klidně si servery vyměň nebo přidej.
#
# for server in servery:
#     Pro každé jméno v seznamu proveď odsazené řádky.
#
#     zacatek = time.perf_counter()
#     Stopky: přesný čas teď, v sekundách.
#
#     spojeni = socket.create_connection((server, 443), timeout=5)
#     Naváže TCP spojení se serverem na portu 443. Uvnitř se stane hodně:
#     DNS přeloží jméno, pošle se paket se žádostí o spojení, server
#     odpoví, počítač potvrdí. Timeout 5 říká: když do pěti sekund nic,
#     vzdej to a vyhoď chybu.
#
#     konec = time.perf_counter()
#     Stopky podruhé.
#
#     spojeni.close()
#     Spojení zase zavřeme, nic po něm neposíláme. Serveru je to jedno.
#
#     ms = (konec - zacatek) * 1000
#     Rozdíl v sekundách krát tisíc = milisekundy.
#
#     print(f"{server:<16} {ms:7.1f} ms")
#     f-string z ptaní 5: jméno vlevo na 16 znaků, číslo vpravo na 7 znaků
#     s jedním desetinným místem.
#
# Když to spadne na jednom serveru (TimeoutError nebo ConnectionRefused),
# školní síť ho nejspíš nepouští. Smaž ho ze seznamu a spusť znovu.
#
# Co si z toho odnést: zpoždění roste se vzdáleností a s počtem
# směrovačů po cestě. Do Brna jednotky milisekund, do Brazílie stovky.
# Příkaz ping měří totéž, jen jiným druhem paketu.
