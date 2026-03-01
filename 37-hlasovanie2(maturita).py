subor = open('hlasovanie_1(37).txt', 'r')
vsetky_hlasy = []

for riadok in subor:
    cislo = riadok.strip()
    if cislo != '':
        vsetky_hlasy.append(cislo)
subor.close()

# Vypis celkoveho poctu SMS
celkovy_pocet = len(vsetky_hlasy)
print('Celkovy pocet zaslanych SMS:', celkovy_pocet)

# 2. a 3. Vytvaranie suborov pre sutaziacich 5220 az 5229
for sutaziaci in range(5220, 5230):
    # Premenna sutaziaci sa meni od 5220 do 5229
    meno_suboru = str(sutaziaci) + '(37).txt'
    vystup = open(meno_suboru, 'w')
    
    # Prechadzame zoznam vsetkych hlasov
    for i in range(len(vsetky_hlasy)):
        # Ak sa hlas v zozname zhoduje s cislom sutaziaceho
        if vsetky_hlasy[i] == str(sutaziaci):
            # Poradove cislo je index + 1 (lebo indexujeme od 0)
            vystup.write(str(i + 1) + '\n')
            
    vystup.close()

print('Subory 5220.txt az 5229.txt boli vytvorene.')