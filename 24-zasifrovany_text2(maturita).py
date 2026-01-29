import random

vstup = open('vstupny_text.txt', 'r', encoding='utf-8')
vystup = open('zasifrovany_text_2.txt', 'w', encoding='utf-8')

for riadok in vstup:
    #vygenerujeme nahodny posun pre tento riadok
    posun = random.randint(1, 25)
    
    #zistim pismeno ktore reprezentuje posun (1='a', 2='b'...)
    znak_posunu = chr(ord('a') + posun - 1)
    
    novy_riadok = znak_posunu #na zaciatok dame kod posunu
    
    for znak in riadok:
        if 'a' <= znak <= 'z':
            povodna = ord(znak) - ord('a')
            nova = (povodna + posun) % 26
            novy_riadok = novy_riadok + chr(nova + ord('a'))
        else:
            novy_riadok = novy_riadok + znak
            
    vystup.write(novy_riadok)

vstup.close()
vystup.close()
print("Hotovo. Text bol zašifrovaný.")