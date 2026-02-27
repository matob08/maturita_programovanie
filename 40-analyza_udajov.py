# ukazka vstupneho suboru
ukazka = ("15:38 áno\n15:39 áno\n14:33 áno\n08:38 áno\n07:42 áno\n15:20 áno\n")
with open("spokojnost_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

vstupny_subor = "spokojnost_1.txt"

celkovy_pocet = 0
hodiny = {}
dni = {}

aktualny_den = 1
predchadzajuca_hodina = -1

subor = open(vstupny_subor, "r", encoding="utf-8")
riadok = subor.readline()
while riadok != "":
    riadok = riadok.strip()
    if riadok != "":
        cas, reakcia = riadok.split(" ", 1)
        hodina = int(cas.split(":")[0])

        # novy den ak hodina klesla
        if hodina < predchadzajuca_hodina:
            aktualny_den += 1

        celkovy_pocet += 1
        hodiny[hodina] = hodiny.get(hodina, 0) + 1
        dni[aktualny_den] = dni.get(aktualny_den, 0) + 1

        predchadzajuca_hodina = hodina
    riadok = subor.readline()
subor.close()

# vypis
for den in sorted(dni.keys()):
    print(f"{den}. den - pocet reakcii:{dni[den]}")

print("Pocet vsetkych vyjadreni:", celkovy_pocet)

for hodina in sorted(hodiny.keys()):
    print(f"Hodina:{hodina} Reakcii zakaznikov:{hodiny[hodina]}")

print("Pocet dni:", len(dni))
