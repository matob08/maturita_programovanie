# Funkcia na dekodovanie cisiel na 0 a 1
def spracuj_riadok(riadok):
    cisla = riadok.split()
    vysledok = ''
    znak = '0' # zaciname ciernou (0)
    
    for cislo in cisla:
        pocet = int(cislo)
        vysledok = vysledok + znak * pocet
        
        # striedanie 0 a 1
        if znak == '0':
            znak = '1'
        else:
            znak = '0'
            
    return vysledok

# Otvorenie suborov
vstup = open('dekompresia_obrazka_1(34).txt', 'r')
vystup = open('dekompresia_obrazka_vystup(34).txt', 'w')

# Nacitanie rozmerov z prveho riadku
prvy = vstup.readline().strip()
rozmery = prvy.split()
sirka = int(rozmery[0])
vyska = int(rozmery[1])

# Vypis informacii
print('Sirka:', sirka)
print('Vyska:', vyska)
print('Pocet bodov:', sirka * vyska)

# Zapis rozmerov do noveho suboru
vystup.write(str(sirka) + ' ' + str(vyska) + '\n')

# Spracovanie zvysnych riadkov obrazka
for riadok in vstup:
    riadok = riadok.strip()
    if riadok != '':
        novy_riadok = spracuj_riadok(riadok)
        vystup.write(novy_riadok + '\n')

# Zatvorenie suborov
vstup.close()
vystup.close()

print('Hotovo.')