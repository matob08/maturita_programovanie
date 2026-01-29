import random

#otvorim subor na citanie
subor = open('poprehadzovany_text1_vstup.txt', 'r', encoding='utf-8')
vystup = open('poprehadzovany_text1.txt', 'w', encoding='utf-8')

text = subor.read()
slova = text.split() #rozdelime text na slová

novy_text = []

for slovo in slova:
    if len(slovo) > 3: #miesam len ak ma slovo aspon 4 znaky
        prve = slovo[0]
        posledne = slovo[-1]
        stred = list(slovo[1:-1]) #vyberiem stred a spravime z neho zoznam
        random.shuffle(stred)     #pomiesam stred
        
        #zlozime slovo naspat: prve + pomiesany stred + posledne
        nove_slovo = prve + "".join(stred) + posledne
        novy_text.append(nove_slovo)
    else:
        #kratke slova nemiesam
        novy_text.append(slovo)

#spojime slova medzerou a zapisem
vysledok = " ".join(novy_text)
print(vysledok)
vystup.write(vysledok)

subor.close()
vystup.close()