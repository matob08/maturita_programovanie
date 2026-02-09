import tkinter
farby = ["blue", "green", "maroon", "purple", "red", "fuchsia", "yellow"]
canvas = tkinter.Canvas(width = 1000, height = 120, bg = "white")
canvas.pack()

vyraz = input("Zadaj výraz: ")

ok = True
pocet = 0

for znak in vyraz:
    if znak == "(":
        pocet += 1
    elif znak == ")":
        pocet -= 1
        if pocet < 0:
            ok = False
            break

if ok and pocet != 0:
    ok = False

if ok:
    oznam = "Zátvorky sú správne!"
else:
    oznam = "Zátvorky nie sú správne!"

canvas.create_text(500, 90, text = oznam, font = "Arial 20")

if ok:
    y = 3
    ktora = -1
    for znak in vyraz:
        if znak == "(":
            ktora += 1
        if znak == "(" or znak == ")":
            canvas.create_text(y, 3, anchor = "nw", text = znak,font = "Arial 20", fill = farby[ktora])
        else:
            canvas.create_text(y, 3, anchor = "nw", text = znak,font = "Arial 20", fill = "black")
        if znak == ")":
            ktora -= 1
        y += 30

canvas.mainloop()