subor = open('hlasovanie_1.txt', 'r')
hlasy = {}

#inicializacia aby sme mali nuly pre kazde cislo
for i in range(5220, 5230):
    hlasy[str(i)] = 0

#citanie suboru
for riadok in subor:
    cislo = riadok.strip() #odstranime "enter" na konci
    if cislo in hlasy:
        hlasy[cislo] = hlasy[cislo] + 1

subor.close()

print("Výsledky hlasovania:")
for k in hlasy:
    print("Číslo", k, "získalo", hlasy[k], "hlasov")