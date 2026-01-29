import random

#nacitanie tipov od uzivatela
vstup = input("Zadaj 6 čísel (oddelených medzerou): ")
moje_cisla = []
for x in vstup.split():
    moje_cisla.append(int(x))

#zrebovanie 6 unikatnych cisel
vyzrebovane = random.sample(range(1, 50), 6)
print("Vyžrebované čísla:", vyzrebovane)

#porovnanie mojich cisel
uhadnute = 0
for cislo in moje_cisla:
    if cislo in vyzrebovane:
        uhadnute = uhadnute + 1
print("Počet uhadnutých čísel:", uhadnute)

#kontrola ostatnych zo suboru
subor = open('loteria_1.txt', 'r') #alebo loteria_2.txt
pocty_vyhier = [0, 0, 0, 0, 0, 0, 0] #index 0 až 6 pre pocet zasahov

for riadok in subor:
    #nacitame cisla cudzieho tiketu
    tiket = []
    for x in riadok.split():
        tiket.append(int(x))
    
    #zistime kolko uhadol tento tiket
    zasahy = 0
    for c in tiket:
        if c in vyzrebovane:
            zasahy = zasahy + 1
            
    #zvysime pocitadlo pre dany pocet zasahov
    pocty_vyhier[zasahy] = pocty_vyhier[zasahy] + 1

subor.close()

#vypis statistiky
print("Štatistika ostatných tipujúcich:")
for i in range(1, 7):
    print("Počet ľudí, čo uhádli", i, "čísel:", pocty_vyhier[i])