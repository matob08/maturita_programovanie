# ukazka vstupneho suboru
ukazka = ("08:39 áno\n06:47 áno\n10:52 áno\n14:55 nie\n15:30 nie\n10:53 áno\n"
          "08:15 áno\n08:22 áno\n10:05 nie\n14:10 áno\n15:45 áno\n15:50 nie\n")
with open("spokojnost_1.txt", "w", encoding="utf-8") as f:
    f.write(ukazka)

vstupny_subor = "spokojnost_1.txt"

# pocitadla po hodinach
spokojni = {}
nespokojen = {}
celkovy_pocet = 0

subor = open(vstupny_subor, "r", encoding="utf-8")
riadok = subor.readline()
while riadok != "":
    riadok = riadok.strip()
    if riadok != "":
        cas, reakcia = riadok.split(" ", 1)
        hodina = int(cas.split(":")[0])
        celkovy_pocet += 1
        if reakcia == "áno":
            spokojni[hodina] = spokojni.get(hodina, 0) + 1
        else:
            nespokojen[hodina] = nespokojen.get(hodina, 0) + 1
    riadok = subor.readline()
subor.close()

# vypis vysledkov
print("Celkovy pocet vyjadreni:", celkovy_pocet)

hodina_max_sp = max(spokojni, key=spokojni.get)
print("Hodina s najviac spokojnymi:", hodina_max_sp, "- pocet:", spokojni[hodina_max_sp])

if nespokojen:
    hodina_max_nesp = max(nespokojen, key=nespokojen.get)
    print("Hodina s najviac nespokojnymi:", hodina_max_nesp, "- pocet:", nespokojen[hodina_max_nesp])

# percenta spokojnosti po hodinach
print("\nPercenta spokojnosti podla hodin:")
for hodina in sorted(set(list(spokojni.keys()) + list(nespokojen.keys()))):
    sp = spokojni.get(hodina, 0)
    nesp = nespokojen.get(hodina, 0)
    percento = round(sp / (sp + nesp) * 100, 1)
    print(f"  Hodina {hodina:02d}: {percento}% ({sp} spokojnych, {nesp} nespokojnych)")
