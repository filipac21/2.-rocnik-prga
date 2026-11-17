# Síť 3 — síť, maska a soused
#
# JAK TO FUNGUJE — přečti si to dřív, než začneš opisovat
# ------------------------------------------------------
# IP adresa má dvě části: která síť a který počítač v ní. Kde končí
# jedna a začíná druhá, říká prefix za lomítkem: 192.168.1.10/24
# znamená, že prvních 24 bitů (tři čísla) je adresa sítě a zbylých
# 8 bitů (poslední číslo) je počítač. Totéž se dá zapsat maskou
# 255.255.255.0. Z toho plyne, kolik zařízení se do sítě vejde a jestli
# je soused ve stejné síti, nebo k němu musí paket přes směrovač.
#
# Knihovna ipaddress to všechno spočítá za tebe. Tvoje práce je číst,
# co vypsala, a měnit prefix.
#
# >>> KÓD — tohle opisuješ
import ipaddress

zapis = input("IP adresa s prefixem (třeba 192.168.1.10/24): ")
rozhrani = ipaddress.ip_interface(zapis)
sit = rozhrani.network

print("Adresa počítače:   ", rozhrani.ip)
print("Adresa sítě:       ", sit.network_address)
print("Maska sítě:        ", sit.netmask)
print("Všesměrová adresa: ", sit.broadcast_address)
print("Adres v síti celkem:", sit.num_addresses, "z toho pro zařízení:", sit.num_addresses - 2)

soused = ipaddress.ip_address(input("Adresa souseda: "))
print("Soused je ve stejné síti:", soused in sit)
# <<< KÓD
#
# VYSVĚTLENÍ KAŽDÉHO ŘÁDKU — pro toho, kdo programuje poprvé
# ------------------------------------------------------------
# zapis = input("IP adresa s prefixem (třeba 192.168.1.10/24): ")
#     Text jako "192.168.1.10/24". Lomítko a číslo za ním je prefix,
#     počet bitů adresy sítě.
#
# rozhrani = ipaddress.ip_interface(zapis)
#     Rozhraní = adresa počítače i s informací o síti. Z textu udělá
#     objekt, který ví obojí.
#
# sit = rozhrani.network
#     Jen síť, bez konkrétního počítače: 192.168.1.0/24.
#
# print("Adresa počítače:   ", rozhrani.ip)
#     192.168.1.10. Mezery za dvojtečkou v textu jsou jen kvůli zarovnání
#     výpisu.
#
# print("Adresa sítě:       ", sit.network_address)
#     192.168.1.0: bity počítače vynulované. Tahle adresa je jméno celé
#     sítě, žádné zařízení ji mít nesmí.
#
# print("Maska sítě:        ", sit.netmask)
#     255.255.255.0: jedničky tam, kde je adresa sítě, nuly tam, kde
#     počítač. Prefix /24 a maska 255.255.255.0 říkají totéž dvěma
#     způsoby.
#
# print("Všesměrová adresa: ", sit.broadcast_address)
#     192.168.1.255: bity počítače samé jedničky. Paket poslaný sem
#     dostanou všechna zařízení v síti. Taky ji nesmí mít nikdo.
#
# print("Adres v síti celkem:", sit.num_addresses, "z toho pro zařízení:", sit.num_addresses - 2)
#     Pro /24 je 8 bitů pro počítače, 2 na 8 = 256 adres. Dvě padnou na
#     adresu sítě a všesměrovou, zbývá 254 zařízení.
#
# soused = ipaddress.ip_address(input("Adresa souseda: "))
#     Druhý vstup, hned převedený na adresu.
#
# print("Soused je ve stejné síti:", soused in sit)
#     Slovo in se ptá „je prvek v množině?“ a vrací True/False. Když je
#     soused ve stejné síti, počítače si píšou přímo. Když ne, musí paket
#     přes směrovač, který ví, kam dál.
#
# Co si z toho odnést: adresa = síť + počítač, hranici určuje prefix
# nebo maska. Z prefixu plyne velikost sítě: 2 na (32 − prefix) adres,
# minus dvě.
