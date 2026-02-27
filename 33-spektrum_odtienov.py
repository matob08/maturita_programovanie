import tkinter
canvas = tkinter.Canvas(height = 450, width = 520, bg = 'white')
canvas.pack()

def historgram(hodnoty, mierka):
    for i in range(256):
        canvas.create_rectangle(i*2, 500, i*2 + 2, 500 - hodnoty[i] / mierka, width = 0, fill = 'gray')

subor = open('ciernobiely_obrazok(31).txt', 'r')
riadok = subor.readline()
velkost = riadok.split()
sirka = int(velkost[0])
vyska = int(velkost[1])

odtiene = [0] * 256
for i in range(vyska):
    riadok = subor.readline()
    for i in range(sirka):
        farba = riadok[i*2 : i*2 + 2]
        dec_farba = int(farba, 16)
        odtiene[dec_farba] += 1
subor.close()

max_vyskyt = max(odtiene)
mierka = (max_vyskyt // 500) + 1
historgram(odtiene, mierka)

canvas.mainloop()