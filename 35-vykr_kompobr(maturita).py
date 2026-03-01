import tkinter
canvas = tkinter.Canvas()
canvas.pack()

je_negativ = False

def kresli():
    # Zmazanie vsetkeho pred kreslenim
    canvas.delete('all')
    
    subor = open('komprimovany_obrazok_1(35).txt', 'r')
    
    prvy_riadok = subor.readline().strip()
    rozmery = prvy_riadok.split()
    sirka = int(rozmery[0])
    vyska = int(rozmery[1])
    canvas['width'] = sirka
    canvas['height'] = vyska
    
    y = 0
    # Prechadzanie ostatnych riadkov suboru (samotny obrazok)
    for riadok in subor:
        riadok = riadok.strip()
        if riadok != '':
            cisla = riadok.split()
            x = 0
            
            # Nastavenie pociatocnej farby pre dany riadok
            if je_negativ == False:
                farba = 'black'
            else:
                farba = 'white'
                
            # Prechadzanie cisiel v riadku
            for cislo in cisla:
                pocet = int(cislo)
                
                # Kreslenie obdlznikov 1x1 pixel
                for i in range(pocet):
                    canvas.create_rectangle(x, y, x+1, y+1, fill=farba, outline='')
                    x = x + 1
                    
                # Striedanie farieb pre dalsi blok pixelov
                if farba == 'black':
                    farba = 'white'
                else:
                    farba = 'black'
                    
        # Posun na dalsi riadok
        y = y + 1
        
    # Zatvorenie suboru
    subor.close()

# Funkcia pre tlacidlo - zmeni stav a prekresli
def prepni_negativ():
    global je_negativ
    
    # Obratenie hodnoty
    if je_negativ == False:
        je_negativ = True
    else:
        je_negativ = False
        
    # Znovu zavolame funkciu na kreslenie
    kresli()

# Vytvorenie tlacidla na prepinanie
button1 = tkinter.Button(text='Negativ', command=prepni_negativ)
button1.pack()

# Prve vykreslenie obrazka po spusteni programu
kresli()

canvas.mainloop()