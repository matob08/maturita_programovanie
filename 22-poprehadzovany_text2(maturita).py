import random

def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return "".join(pismenka)

subor = open('poprehadzovany_text_vstup2.txt', 'r', encoding='utf-8')
text = subor.read()
subor.close()

vysledok = ""
slovo_temp = ""

for znak in text:
    #ak je znak pismeno, pridame ho do docasneho slova
    if znak.isalpha():
        slovo_temp = slovo_temp + znak
    else:
        #ak prisiel iny znak spracujem nazbierane slovo
        if len(slovo_temp) > 0:
            if len(slovo_temp) > 3:
                stred = slovo_temp[1:-1]
                novy_stred = pomiesaj(stred)
                hotove_slovo = slovo_temp[0] + novy_stred + slovo_temp[-1]
                vysledok = vysledok + hotove_slovo
            else:
                vysledok = vysledok + slovo_temp
            
            slovo_temp = "" #vycistime pre dalsie slovo
        
        #pridam ten znak
        vysledok = vysledok + znak

print(vysledok)