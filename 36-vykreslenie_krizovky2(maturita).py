import tkinter

canvas = tkinter.Canvas(width=800, height=500)
canvas.pack()

# Nacitanie obsahu suboru do pamate
subor = open('krizovka2_1(36).txt', 'r')
tajnicka = subor.readline().strip().upper() # prvy riadok je tajnicka
slova = []

for riadok in subor:
    slovo = riadok.strip().upper()
    if slovo != '':
        slova.append(slovo) # pridanie slov do zoznamu
subor.close()

def vykresli_krizovku(x_tajnicky, y_start, d, vyplnena):
    y = y_start
    
    # Prechadzame pismena tajnicky a prislusne slova
    for i in range(len(tajnicka)):
        hladane_pismeno = tajnicka[i]
        aktualne_slovo = slova[i]
        
        # Zistenie, na ktorom indexe v slove sa nachadza pismeno tajnicky
        pozicia = aktualne_slovo.find(hladane_pismeno)
        
        # Vypocet startovacieho X pre dany riadok
        x_riadku = x_tajnicky - (pozicia * d)
        
        # Kreslenie jednotlivych stvorcekov slova
        for j in range(len(aktualne_slovo)):
            # Farba: tajnicka bude seda, ostatne biele
            if j == pozicia:
                farba = 'lightgrey'
            else:
                farba = 'white'
            
            # Vykreslenie stvorceka
            canvas.create_rectangle(x_riadku, y, x_riadku + d, y + d, fill=farba)
            
            # Ak je krizovka vyplnena, dopiseme pismeno
            if vyplnena == True:
                canvas.create_text(x_riadku + d/2, y + d/2, text=aktualne_slovo[j], font='Arial 12')
            
            x_riadku = x_riadku + d
            
        y = y + d # posun na dalsi riadok

# Pouzitie funkcie na vykreslenie dvoch verzii vedla seba
# Nevyplnena krizovka vlavo
vykresli_krizovku(150, 50, 30, False)

# Vyplnena krizovka vpravo
vykresli_krizovku(500, 50, 30, True)

canvas.mainloop()