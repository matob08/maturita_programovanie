import random

vstup = open('virus.txt', 'r', encoding='utf-8')
vystup = open('virus_vystup.txt', 'w', encoding='utf-8')

for riadok in vstup:
    slova = riadok.split()
    novy_riadok = []
    
    for slovo in slova:
        #nahodne 0 alebo 1 ak 1 otocime slovo
        if random.randint(0, 1) == 1:
            otocene = slovo[::-1]
            novy_riadok.append(otocene)
        else:
            novy_riadok.append(slovo)
            
    #spojime slova spat do vety
    veta = " ".join(novy_riadok)
    print(veta)
    vystup.write(veta + '\n')

vstup.close()
vystup.close()