import tkinter
canvas = tkinter.Canvas(width=480, height=520)
canvas.pack()

celkovy_pocet_nie = 0
nespokojni_podla_hodin = {}

subor = open('spokojnost_1(38-39).txt', 'r', encoding='utf-8')

for riadok in subor:
    riadok = riadok.strip()
    if riadok != '':
        casti = riadok.split()
        cas = casti[0]
        hlas = casti[1]
        
        # Zaujimaju nas len negativne vyjadrenia
        if hlas == 'nie':
            celkovy_pocet_nie = celkovy_pocet_nie + 1
            hodina = cas[:2] # rez stringu pre hodinu
            
            # Pripositanie do slovnika
            nespokojni_podla_hodin[hodina] = nespokojni_podla_hodin.get(hodina, 0) + 1
subor.close()

print('Celkovy pocet negativnych vyjadreni:', celkovy_pocet_nie)

# Hladanie hodiny s najvacsim poctom nespokojnych
max_pocet = 0
top_hodina = ''
for h in nespokojni_podla_hodin:
    if nespokojni_podla_hodin[h] > max_pocet:
        max_pocet = nespokojni_podla_hodin[h]
        top_hodina = h

print('Najviac nespokojnych bolo v hodine', top_hodina, 'pocet:', max_pocet)
print('-' * 30)

print('Pocet nespokojnych v hodinach:')
zoradene_hodiny = sorted(nespokojni_podla_hodin.keys())
for h in zoradene_hodiny:
    print('Hodina {}: {} nespokojnych'.format(h, nespokojni_podla_hodin[h]))

#Vykreslenie histogramu
sirka_stlpca = 20
spodna_hranica = 500 # y suradnica, kde stlpce zacinaju

for i in range(24):
    # Premena cisla i na format '00' az '23'
    if i < 10:
        h_str = '0' + str(i)
    else:
        h_str = str(i)
    
    # Ziskanie poctu pre danu hodinu (ak nie je v slovniku, tak 0)
    pocet = nespokojni_podla_hodin.get(h_str, 0)
    
    # Suradnice pre stlpec
    x1 = i * sirka_stlpca
    x2 = x1 + sirka_stlpca
    y1 = spodna_hranica - (pocet * 10) # 1 nespokojny = 10 pixelov vyska
    y2 = spodna_hranica
    
    # Vykreslenie stlpca (len ak je pocet > 0)
    if pocet > 0:
        canvas.create_rectangle(x1 + 2, y1, x2 - 2, y2, fill='red')
    
    # Vykreslenie popisu hodiny na os X
    canvas.create_text(x1 + 10, y2 + 10, text=h_str, font='Arial 8')
    
canvas.mainloop()