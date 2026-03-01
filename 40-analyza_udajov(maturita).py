subor = open('analyza_udajov(40).txt', 'r', encoding='utf-8')

celkovy_pocet = 0
hodiny_stats = {}
pocty_v_dniach = []
aktualny_den_reakcie = 0
predosly_cas = ""

for riadok in subor:
    riadok = riadok.strip()
    if riadok != "":
        celkovy_pocet = celkovy_pocet + 1
        casti = riadok.split()
        cas = casti[0] 
        
        #Spracovanie hodiny
        hodina_text = cas[:2]
        hodina = int(hodina_text)
        hodiny_stats[hodina] = hodiny_stats.get(hodina, 0) + 1
        
        #Detekcia noveho dna
        # Ak je aktualny cas skor ako predosly, znamena to novy den
        if predosly_cas != "" and cas < predosly_cas:
            pocty_v_dniach.append(aktualny_den_reakcie)
            aktualny_den_reakcie = 1
        else:
            aktualny_den_reakcie = aktualny_den_reakcie + 1
            
        predosly_cas = cas

#Pridanie posledneho dna po dopisani vsetkych riadkov
if aktualny_den_reakcie > 0:
    pocty_v_dniach.append(aktualny_den_reakcie)
subor.close()

# Vypis poctov po dnoch
for i in range(len(pocty_v_dniach)):
    print('{}. deň - počet reakcií:{}'.format(i + 1, pocty_v_dniach[i]))

print('Počet všetkých vyjadrení:', celkovy_pocet)

# Vypis poctov v hodinach
zoradene_hodiny = sorted(hodiny_stats.keys())
for h in zoradene_hodiny:
    print('Hodina:{} Reakcií zákazníkov:{}'.format(h, hodiny_stats[h]))

print('Počet dní:', len(pocty_v_dniach))