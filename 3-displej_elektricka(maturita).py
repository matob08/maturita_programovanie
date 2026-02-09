import tkinter
canvas = tkinter.Canvas(width=600, height=100, bg = "black")
canvas.pack()

def animacia():
    global nazov
    nazov = nazov[1:] + nazov[0]
    canvas.delete("all")
    canvas.create_text(300,50,text = nazov, fill = "red", font = ("Courier New", 35, "bold"))
    canvas.after(100,animacia)

def vypis(index, zastavky, konecna):
    global nazov
    nazov = zastavky [index] + ' '
    if konecna:
        nazov += ' - KONEČNÁ, VYSTUPOVAŤ!   '
    nazov = nazov + ' ' * (20 - len(nazov))

def dalsie(event):
    global aktualna, konecna
    if not konecna:
        aktualna += 1
        if aktualna == len(zastavky) - 1:
            konecna = True
        vypis(aktualna, zastavky, konecna) 

subor =open("zastavky.txt", "r", encoding="utf-8")
zastavky = []
for zastavka in subor:
    zastavky.append(zastavka.strip())
aktualna = 0
konecna = False
nazov = ''
vypis(aktualna, zastavky, konecna)
animacia()
print(zastavky)
canvas.bind_all('<Key>', dalsie)

canvas.mainloop()