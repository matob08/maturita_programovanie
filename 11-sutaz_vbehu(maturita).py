subor = open("sutaz_vbehu.txt", "r")
sportovci = []

for riadok in subor:
    udaje = riadok.strip().split()
    sportovci.append((udaje[0], int(udaje[1])))

print ("Počet zúčastnených športovcov:", len(sportovci))
naj = sportovci[0][1]
for prvok in sportovci:
    if prvok[1] < naj:
        naj = prvok[1]
        vitaz = prvok[0]

print("Najlepší športovec:", vitaz, "s časom", naj // 60, "min.", naj % 60, "sek.")