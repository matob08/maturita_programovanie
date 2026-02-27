# ukazka vstupneho suboru
ukazka = "5225\n5227\n5225\n5224\n5225\n5227\n5220\n5223\n5225\n5221\n"
with open("hlasovanie_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

vstupny_subor = "hlasovanie_1.txt"

# nacitanie vsetkych SMS
subor = open(vstupny_subor, "r", encoding="utf-8")
vsetky_sms = []
riadok = subor.readline()
while riadok != "":
    cislo = riadok.strip()
    if cislo != "":
        vsetky_sms.append(cislo)
    riadok = subor.readline()
subor.close()

print("Celkovy pocet SMS:", len(vsetky_sms))

# vytvorenie vystupnych suborov pre kazdého sutaziaceho
for sut_cislo in range(5220, 5230):
    vystup = open(str(sut_cislo) + ".txt", "w", encoding="utf-8")
    for poradie, sms in enumerate(vsetky_sms):
        if sms == str(sut_cislo):
            vystup.write(str(poradie + 1) + "\n")
    vystup.close()

print("Subory vytvorene.")

# overenie
print("\n5225.txt:")
with open("5225.txt", "r") as f:
    obsah = f.read()
    print(obsah if obsah else "(prazdny)")

print("5220.txt:")
with open("5220.txt", "r") as f:
    obsah = f.read()
    print(obsah if obsah else "(prazdny)")
