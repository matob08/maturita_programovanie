subor = open("bus_vytazenost.txt",encoding="utf-8")

kapacita = int(subor.readline())

zoznam = []
pretazenie = []
pocet = 0
naj = 0

for riadok in subor:
    udaje = riadok.split()
    if len(udaje) == 3:
        nazov = udaje[2]
    else:
        nazov = udaje[2] + " " + udaje[3]
    pocet += int(udaje[0])
    pocet -= int(udaje[1])
    if pocet > kapacita:
        pretazenie.append(nazov)
        if pocet - kapacita > naj:
            naj = pocet - kapacita
    zoznam.append(nazov)
    
print("Kapacita autobusu:", kapacita)
print("Počet zastávok:", len(zoznam))
print("Zastávky na trase: ", end ="")

for zastavka in zoznam:
    print(zastavka, end=", ")
print("Autobus bol preplnený nad povolenú kapacitu po vyjdení zo zastávok:")

for zastavka in pretazenie:
    print(zastavka)
print("Najväčšie preťaženie o", naj, "ľudí.")