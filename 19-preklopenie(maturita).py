import tkinter as tk

# Veľkosť štvorčeka pre jeden pixel
strana = 20

# Načítanie obrázka zo súboru
def nacitaj_obrazok(subor):
    with open(subor, "r") as f:
        rozmery = f.readline().strip().split()
        sirka = int(rozmery[0])
        vyska = int(rozmery[1])
        obrazok = []
        for _ in range(vyska):
            riadok = list(map(int, f.readline().strip().split()))
            obrazok.append(riadok)
    return sirka, vyska, obrazok

# Vykreslenie obrázka
def vykresli_obrazok(obrazok):
    platno.delete("vsetko")  # vymaže všetko z plátna
    for riadok in range(len(obrazok)):
        for stlpec in range(len(obrazok[0])):
            farba = "black" if obrazok[riadok][stlpec] == 1 else "white"
            x1 = stlpec * strana
            y1 = riadok * strana
            x2 = x1 + strana
            y2 = y1 + strana
            platno.create_rectangle(x1, y1, x2, y2, fill=farba, outline="gray", tags="vsetko")

# Funkcia na preklopenie obrázka podľa osi Y
def zobraz_preklopeny():
    obrazok_preklopeny = [list(reversed(riadok)) for riadok in obrazok]
    vykresli_obrazok(obrazok_preklopeny)

# Funkcia na zobrazenie pôvodného obrázka
def zobraz_povodny():
    vykresli_obrazok(obrazok)

# Načítanie obrázka
sirka, vyska, obrazok = nacitaj_obrazok("Maturita/preklopenie_obrazka.txt")

# Výpočet počtu pixelov a jednotiek
pocet_pixelov = sirka * vyska
pocet_jednotiek = sum(riadok.count(1) for riadok in obrazok)
print(f"Počet pixelov: {pocet_pixelov}")
print(f"Počet jednotiek: {pocet_jednotiek}")

# Vytvorenie okna
okno = tk.Tk()
okno.title("Preklopenie obrázka")

# Plátno
platno = tk.Canvas(okno, width=sirka * strana, height=vyska * strana, bg="white")
platno.pack()

# Tlačidlá
tlacidlo_povodny = tk.Button(okno, text="Zobraziť pôvodný", command=zobraz_povodny)
tlacidlo_povodny.pack()

tlacidlo_preklopeny = tk.Button(okno, text="Zobraziť preklopený", command=zobraz_preklopeny)
tlacidlo_preklopeny.pack()

# Na začiatku zobrazíme pôvodný
zobraz_povodny()

okno.mainloop()