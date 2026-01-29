def spracuj_riadok(riadok):
    if not riadok:
        return ""
    
    vysledok = ""
    aktualny_znak = riadok[0]
    pocet = 0
    
    for znak in riadok:
        if znak == aktualny_znak:
            pocet = pocet + 1
        else:
            #zapiseme pocet predoslych znakov
            vysledok = vysledok + str(pocet) + " "
            #zmenime sledovany znak
            aktualny_znak = znak
            pocet = 1
            
    vysledok = vysledok + str(pocet) #dopiseme posledny skupinu
    return vysledok

#hlavny program
subor = open('kompresia_obrazka_1.txt', 'r')
rozmery = subor.readline() #prvy riadok su rozmery
print("Rozmery:", rozmery.strip())

cislo_riadku = 1
for riadok_suboru in subor:
    kompresia = spracuj_riadok(riadok_suboru.strip())
    print("Riadok", cislo_riadku, ":", kompresia)
    cislo_riadku = cislo_riadku + 1

subor.close()