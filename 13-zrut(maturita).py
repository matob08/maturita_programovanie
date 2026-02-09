from random import *
from math import *
import tkinter

N = 4
r = 20

def stlac(event):
    global dx, dy
    if event.char == 'w':
        dx, dy = 0, -2
    elif event.char == 's':
        dx, dy = 0, 2
    elif event.char == 'a':
        dx, dy = -2, 0
    elif event.char == 'd':
        dx, dy = 2, 0

def run():
    global zx, zy
    zx += dx
    zy += dy
    canvas.move(zrut, dx, dy)
    for i in range(len(kruhy)):
        if sqrt((kruhy[i][0] - zx) ** 2 + (kruhy[i][1] - zy) ** 2) <= 2 * r:
            canvas.delete(kruhy[i][2])
            kruhy.pop(i)
            break
    if len(kruhy) > 0:
        canvas.after(50, run)
    else:
        canvas.create_text(250, 250, text='Všetky jabĺčka sú zjedené!',
                           font='Arial 30')

canvas = tkinter.Canvas(width=500, height=500, bg='white')
canvas.pack()

zx, zy = r, r
zrut = canvas.create_oval(zx-r, zy-r, zx+r, zy+r, width=0, fill='blue')
dx, dy = 2, 0

kruhy = []
for i in range(N):
    x, y = randint(r * 3, 500 - r), randint(r * 3, 500 - r)
    kruhy.append((x, y, canvas.create_oval(x - r, y - r, x + r, y + r,
                  width=0, fill='red')))

canvas.focus_set()
canvas.bind('<Key>', stlac)
canvas.after(10, run)

canvas.mainloop()