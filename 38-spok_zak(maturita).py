celkovy_pocet = 0
spokojni = {}
nespokojni = {}
vsetci_v_hodine = {}

subor = open('spokojnost_1(38-39).txt', 'r', encoding='utf-8')

for riadok in subor:
    riadok = riadok.strip()
    if riadok != '':
        celkovy_pocet = celkovy_pocet + 1
        
        # Rozdelenie riadku na casti
        casti = riadok.split()
        cas = casti[0]
        hlas = casti[1]
        
        # Ziskanie hodiny 
        hodina = cas[:2]
        
        # Zapocitanie celkoveho poctu hlasov v hodine
        vsetci_v_hodine[hodina] = vsetci_v_hodine.get(hodina, 0) + 1
        
        # Kontrola hlasu
        if 'áno' in hlas:
            spokojni[hodina] = spokojni.get(hodina, 0) + 1
        else:
            nespokojni[hodina] = nespokojni.get(hodina, 0) + 1

subor.close()

#Hladanie hodiny s najviac spokojnymi
max_spok = 0
hodina_spok = ''
for h in spokojni:
    if spokojni[h] > max_spok:
        max_spok = spokojni[h]
        hodina_spok = h

#Hladanie hodiny s najviac nespokojnymi
max_nesp = 0
hodina_nesp = ''
for h in nespokojni:
    if nespokojni[h] > max_nesp:
        max_nesp = nespokojni[h]
        hodina_nesp = h

print('Celkovy pocet vyjadreni:', celkovy_pocet)
print('Najviac spokojnych bolo v hodine', hodina_spok, 'pocet:', max_spok)
print('Najviac nespokojnych bolo v hodine', hodina_nesp, 'pocet:', max_nesp)
print('-' * 40)

print('Percenta spokojnosti pre jednotlive hodiny:')

#Zoradenie hodin podla casu
zoznam_hodin = sorted(vsetci_v_hodine.keys())

for h in zoznam_hodin:
    pocet_spok = spokojni.get(h, 0)
    spolu_v_hodine = vsetci_v_hodine[h]
    
    percento = (pocet_spok / spolu_v_hodine) * 100

    print('Hodina {}: {:.1f} %'.format(h, percento))