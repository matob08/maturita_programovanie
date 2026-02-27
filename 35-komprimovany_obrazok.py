import tkinter

# ukazka vstupneho suboru
ukazka = "20 5\n0 3 2 2 8 5\n2 3 1 1 3 8 2\n0 20\n20\n7 5 5 3\n"
with open("komprimovany_obrazok_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

vstupny_subor = "komprimovany_obrazok_1.txt"

# nacitanie rozmerov
subor = open(vstupny_subor, "r", encoding="utf-8")
sirka, vyska = map(int, subor.readline().strip().split())
subor.close()

root = tkinter.Tk()
root.title("Komprimovany obrazok")

canvas = tkinter.Canvas(root, width=sirka, height=vyska, bg="white")
canvas.pack()


def nakresli_riadok(y, riadok, negativ=False):
    # vykresli jeden riadok zo zakodovaneho retazca
    cisla = list(map(int, riadok.strip().split()))
    x = 0
    for i, pocet in enumerate(cisla):
        if i % 2 == 0:
            farba = "white" if negativ else "black"
        else:
            farba = "black" if negativ else "white"
        if pocet > 0:
            canvas.create_rectangle(x, y, x + pocet, y + 1, fill=farba, outline="")
        x += pocet


def nakresli_obrazok(negativ=False):
    # precita subor a vykresli cely obrazok
    canvas.delete("all")
    subor = open(vstupny_subor, "r", encoding="utf-8")
    subor.readline()
    y = 0
    riadok = subor.readline()
    while riadok != "":
        nakresli_riadok(y, riadok, negativ)
        y += 1
        riadok = subor.readline()
    subor.close()


def klik_negativ():
    nakresli_obrazok(negativ=True)


tlacidlo = tkinter.Button(root, text="negativ", command=klik_negativ)
tlacidlo.pack()

nakresli_obrazok()
root.mainloop()
