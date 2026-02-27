def spracuj_riadok(riadok):
    # dekoduje jeden RLE riadok na retazec 0 a 1
    cisla = list(map(int, riadok.strip().split()))
    vystup = ""
    for i, pocet in enumerate(cisla):
        if i % 2 == 0:
            vystup += "0" * pocet
        else:
            vystup += "1" * pocet
    return vystup


# ukazka vstupneho suboru
ukazka = "20 5\n0 3 2 2 8 5\n2 3 1 1 3 8 2\n0 20\n20\n7 5 5 3\n"
with open("dekompresia_obrazka_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

vstupny_subor = "dekompresia_obrazka_1.txt"
vystupny_subor = "dekompresia_obrazka_vystup.txt"

subor_vstup = open(vstupny_subor, "r", encoding="utf-8")
subor_vystup = open(vystupny_subor, "w", encoding="utf-8")

# rozmery
prvy_riadok = subor_vstup.readline().strip()
sirka, vyska = map(int, prvy_riadok.split())
print("Sirka:", sirka)
print("Vyska:", vyska)
print("Pocet bodov:", sirka * vyska)

subor_vystup.write(str(sirka) + " " + str(vyska) + "\n")

# prvy riadok obrazka
prvy_riadok_obrazka = subor_vstup.readline()
dekomprimovany = spracuj_riadok(prvy_riadok_obrazka)
print("Prvy riadok:", dekomprimovany)
subor_vystup.write(dekomprimovany + "\n")

# zvysok suboru
riadok = subor_vstup.readline()
while riadok != "":
    subor_vystup.write(spracuj_riadok(riadok) + "\n")
    riadok = subor_vstup.readline()

subor_vstup.close()
subor_vystup.close()

print("\nVystupny subor:", vystupny_subor)
with open(vystupny_subor, "r") as f:
    print(f.read())
