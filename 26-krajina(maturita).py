import tkinter, random
canvas = tkinter.Canvas(width=600, height=400, bg='lightblue')
canvas.pack()

def nakresli_krajinu():
    canvas.delete('all') #zmazat stare
    body = [] 
    
    #zaciatok krajiny vlavo dole
    body.append(0)
    body.append(400)
    
    x = 0
    y = 200 #zaciatocna vyska
    
    #generujeme body po celej sirke
    while x < 600:
        #nahodne menime vysku, aby to vyzeralo ako kopec
        zmena = random.randint(-10, 10)
        y = y + zmena
        
        #strazime aby nevysiel mimo obrazovku
        if y < 50: y = 50
        if y > 350: y = 350
            
        body.append(x)
        body.append(y)
        x = x + 20 # Posun doprava
        
    #ukoncenie polygonu vpravo dole
    body.append(600)
    body.append(400)
    
    #vykreslenie zelenej krajiny
    canvas.create_polygon(body, fill='green', outline='black')

#prve kreslenie
nakresli_krajinu()

#po stlaceni medzery prekresli
def prekresli(event):
    nakresli_krajinu()

canvas.bind_all('<space>', prekresli)
tkinter.mainloop()