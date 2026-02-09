import tkinter

# Smerové konštanty
SMERY = ["hore", "vpravo", "dole", "vlavo"]

# Inicializácia hlavného okna
okno = tkinter.Tk()
okno.title("Kresliaci robot")

# Plátno na kreslenie (musíme použiť 'width' a 'height')
canvas = tkinter.Canvas(okno, width=400, height=400, bg="white")
canvas.pack()

# Počiatočná pozícia a smer robota
x = 200
y = 200
smer_index = 0  # 0 = hore

# Funkcia na vykonanie príkazu  
def vykonaj_prikaz():
    global x, y, smer_index
    prikaz = vstup.get()
    casti = prikaz.split()

    if casti[0] == "ciara" and len(casti) == 2:
        dlzka = int(casti[1])
        novy_x, novy_y = x, y

        if SMERY[smer_index] == "hore":
            novy_y -= dlzka
        elif SMERY[smer_index] == "dole":
            novy_y += dlzka
        elif SMERY[smer_index] == "vpravo":
            novy_x += dlzka
        elif SMERY[smer_index] == "vlavo":
            novy_x -= dlzka

        canvas.create_line(x, y, novy_x, novy_y)
        x, y = novy_x, novy_y

    elif prikaz == "vlavo":
        smer_index = (smer_index - 1) % 4
    elif prikaz == "vpravo":
        smer_index = (smer_index + 1) % 4

    vstup.delete(0, tkinter.END)

# Vstupné pole a tlačidlo
vstup = tkinter.Entry(okno)
vstup.pack()

tlacidlo = tkinter.Button(okno, text="Vykonaj", command=vykonaj_prikaz)
tlacidlo.pack()

okno.mainloop()