tajna_tabulka = {0: ' ',1: 'ABC',2: 'DEF',
                3: 'GHI',4: 'JKL',5: 'MNO',
                6: 'PQR',7: 'STU',8: 'VWX',9: 'YZ'}

# Vytvorenie opačného mapovania: znak → číslo
znak_na_cislo = {}
for cislo, znaky in tajna_tabulka.items():
    for znak in znaky:
        znak_na_cislo[znak] = cislo

# Funkcia na zašifrovanie vety
def zasifruj_vetu(veta):
    zasifrovane = []
    frekvencie = [0] * 10

    for znak in veta:
        if znak == ' ':
            cislo = 0
        else:
            cislo = znak_na_cislo.get(znak, 0)

        zasifrovane.append(str(cislo))
        frekvencie[cislo] += 1

    return zasifrovane, frekvencie

# Funkcia na zistenie najčastejšie sa vyskytujúcich čísel
def najcastejsie_cisla(frekvencie):
    maximum = max(frekvencie)
    return [i for i, pocet in enumerate(frekvencie) if pocet == maximum]

veta = input("Zadaj vetu (iba veľké písmená a medzery): ")

zasifrovane, frekvencie = zasifruj_vetu(veta)

print("Zašifrovaná veta:", ' '.join(zasifrovane))

najcastejsie = najcastejsie_cisla(frekvencie)
print("Najčastejšie zvolené políčka:", ', '.join(map(str, najcastejsie)))