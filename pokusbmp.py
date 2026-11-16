import sys
cerne = 0
soubor_cara = open("cara.bmp", "rb"). read()
print(soubor_cara[len(soubor_cara)-1])

for i in range(len(soubor_cara)):
    print(soubor_cara[i])
    if soubor_cara[i] == 0:
        cerne += 1

print("soubor ma delku:", len(soubor_cara))
print("pocet bytu s hodnotou 0:", cerne)