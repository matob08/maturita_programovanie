import tkinter

# ukazka vstupneho suboru
ukazka = ("08:39 áno\n06:47 áno\n10:52 áno\n14:55 nie\n15:30 nie\n10:53 áno\n"
          "08:15 nie\n09:22 nie\n10:05 nie\n14:10 nie\n15:45 nie\n15:50 nie\n"
          "07:10 nie\n07:20 nie\n12:30 nie\n13:10 nie\n")
with open("spokojnost_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

vstupny_subor = "spokojnost_1.txt"

# nacitanie nespokojnych po hodinach
nespokojen = {}
celkovy_pocet_nesp = 0

subor = open(vstupny_subor, "r", encoding="utf-8")
riadok = subor.readline()
while riadok != "":
    riadok = riadok.strip()
    if riadok != "":
        cas, reakcia = riadok.split(" ", 1)
        hodina = int(cas.split(":")[0])
        if reakcia == "nie":
            celkovy_pocet_nesp += 1
            nespokojen[hodina] = nespokojen.get(hodina, 0) + 1
    riadok = subor.readline()
subor.close()

print("Celkovy pocet negativnych:", celkovy_pocet_nesp)
if nespokojen:
    hodina_max = max(nespokojen, key=nespokojen.get)
    print("Hodina s najviac nespokojnymi:", hodina_max, "- pocet:", nespokojen[hodina_max])

# histogram
SIRKA = 480
VYSKA = 520
OKRAJ_SPODU = 40
OKRAJ_ZLAVA = 10
SIRKA_STLPCA = (SIRKA - OKRAJ_ZLAVA) // 24

root = tkinter.Tk()
root.title("Spokojnost zakaznikov 2 - histogram")

canvas = tkinter.Canvas(root, width=SIRKA, height=VYSKA, bg="white")
canvas.pack()

# stlpce pre hodiny 0-23
for hodina in range(24):
    pocet = nespokojen.get(hodina, 0)
    x = OKRAJ_ZLAVA + hodina * SIRKA_STLPCA
    vyska_stlpca = pocet * 30
    if vyska_stlpca > 0:
        canvas.create_rectangle(
            x, VYSKA - OKRAJ_SPODU - vyska_stlpca,
            x + SIRKA_STLPCA - 2, VYSKA - OKRAJ_SPODU,
            fill="red", outline="darkred"
        )
    canvas.create_text(x + SIRKA_STLPCA // 2, VYSKA - OKRAJ_SPODU + 15,
                       text=f"{hodina:02d}", font=("Arial", 7))

# os x
canvas.create_line(OKRAJ_ZLAVA, VYSKA - OKRAJ_SPODU, SIRKA, VYSKA - OKRAJ_SPODU, width=2)

root.mainloop()
