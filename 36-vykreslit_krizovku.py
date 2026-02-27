import tkinter

# ukazka vstupneho suboru
ukazka = "MATURITA\nZOZNAM\nCANVAS\nSTRING\nCYKLUS\nRETURN\nWHILE\nTRUE\nRANDOM\n"
with open("krizovka2_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

# nacitanie dat
subor = open("krizovka2_1.txt", "r", encoding="utf-8")
riadky = []
for riadok in subor:
    riadky.append(riadok.strip())
subor.close()

tajnicka = riadky[0]
slova = riadky[1:]

# pozicie tajnickovych pismen v jednotlivych slovach
pozicie = []
for i, slovo in enumerate(slova):
    pozicie.append(slovo.index(tajnicka[i]))

max_offset = max(pozicie)


def nakresli_krizovku(canvas, start_x, start_y, velkost, vyplnena=True):
    # vykresli krizovku, start_x je x-ova suradnica stlpca s tajnickou
    for i, slovo in enumerate(slova):
        y = start_y + i * velkost
        for j, pismeno in enumerate(slovo):
            x = start_x + (j - pozicie[i]) * velkost
            bg = "yellow" if j == pozicie[i] else "white"
            canvas.create_rectangle(x, y, x + velkost, y + velkost,
                                    fill=bg, outline="black")
            if vyplnena:
                canvas.create_text(x + velkost // 2, y + velkost // 2,
                                   text=pismeno, font=("Arial", velkost // 2))


VEL = 30
pocet_stlpcov = max(len(s) for s in slova) + max_offset + 2
sirka_okna = (pocet_stlpcov + 5) * VEL * 2 + 50
vyska_okna = (len(slova) + 2) * VEL + 50

root = tkinter.Tk()
root.title("Krizovka 2")

canvas = tkinter.Canvas(root, width=sirka_okna, height=vyska_okna, bg="lightgray")
canvas.pack()

# vyplnena vlavo, nevyplnena vpravo
nakresli_krizovku(canvas, max_offset * VEL + 20, 20, VEL, vyplnena=True)
offset_x = (max(len(s) for s in slova) + max_offset + 3) * VEL + 20
nakresli_krizovku(canvas, offset_x + max_offset * VEL, 20, VEL, vyplnena=False)

root.mainloop()
