import tkinter

canvas = tkinter.Canvas(width=650, height=300)
canvas.pack()

pocet_zapaliek = 15

def nakresli_zapalky():
    canvas.delete('all')
    x = 50
    for i in range(pocet_zapaliek):
        canvas.create_line(x, 100, x, 200, width=5, fill='yellow')
        canvas.create_oval(x-5, 95, x+5, 108, fill='brown', outline='brown')
        x = x + 40
        
    canvas.create_text(325, 50, text="Počet zápaliek: " + str(pocet_zapaliek), font='Arial 20')
    if pocet_zapaliek == 0:
         canvas.create_text(325, 250, text="VYHRAL SI!", font='Arial 30', fill='red')

def vezmi(kolko):
    global pocet_zapaliek
    if pocet_zapaliek >= kolko:
        pocet_zapaliek = pocet_zapaliek - kolko
        nakresli_zapalky()

def stlacenie_klavesu(event):
    if event.char in ('1', '2', '3'):
        vezmi(int(event.char))

nakresli_zapalky()
canvas.bind_all('<Key>', stlacenie_klavesu)
tkinter.mainloop()