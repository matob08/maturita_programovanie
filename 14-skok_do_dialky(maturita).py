subor = open("skok_do_dialky.txt", "r")
krajiny = {}
maxdlzka = 0
vitazi = []

for riadok in subor:
    udaje = riadok.split()
    krajiny[udaje[1]] = krajiny.get(udaje[1], 0) + 1
    dlzka = 0
    for i in range(5):
        dlzka = max(dlzka, int(udaje[i+2]))
    if dlzka>maxdlzka:
        maxdlzka = dlzka
        vitazi = [udaje[0]]
    elif dlzka == maxdlzka:
        vitazi.append(udaje[0])

print("Zoznam krajín: ")
for krajina in krajiny:
    print(krajina, end = ", ")
print()

print("Počet športovcov: ")
for dvojica in krajiny.items():
    print(dvojica[0], ":", dvojica[1])

print("Najdlhší skok: ", maxdlzka, "mali skokani: ")
for vitaz in vitazi:
    print(vitaz)