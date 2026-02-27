def spracuj_riadok(vstup):
    pocet = len (vstup) //2
    vystup = ''
    for i in range(pocet):
        odtien = vstup[i*2 : i*2 + 2]
        farba = '0'
        if odtien > '7f':
            farba = '1'
        vystup += farba + ' '
    vystup = vystup[:-1] + '\n'
    return vystup
    
subor = open('ciernobiely_obrazok(31).txt', 'r')
vystup = open('konverzia_suboru1(32).txt', 'w')
riadok = subor.readline()
velkost = riadok.split()
vystup.write(riadok)
sirka = int(velkost[0])
vyska = int(velkost[1])
print('Obrazok ma rozmery {}x{} bodov.'.format(sirka, vyska))
print('Obrazok ma {} pixelov. '.format(sirka * vyska))
riadok = subor.readline()
print(repr(riadok))
spracovanie = spracuj_riadok(riadok)
print(repr(spracovanie))
vystup.write(spracovanie)

for riadok in subor:
    vystup.write(spracuj_riadok(riadok))
subor.close()
vystup.close()