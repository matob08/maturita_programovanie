kluc = input("Zadaj kľúč: ")
text = input("Zadaj text: ")
sifra = ""
dlzka_kluca = len(kluc)

for i in range(len(text)):
    znak = text[i]
    
    #sifrujeme len male pismena
    if 'a' <= znak <= 'z':
        #zistim ktore pismeno z kluca pouzit pomocou zvyšku po delení
        posun_znak = kluc[i % dlzka_kluca]
        
        #vypocitam posun: ord('a') je 97, ak je kluc 'a' posun ma byt 1
        #takze odcitam 'a' dostanem 0 a pripocitam 1
        posun = ord(posun_znak) - ord('a') + 1
        
        #povodna pozicia pismena 0-25
        povodna_hodnota = ord(znak) - ord('a')
        
        #nova pozicia s posunom zvysok po deleni 26 zabezpeci kruzenie abecedy
        nova_hodnota = (povodna_hodnota + posun) % 26
        
        novy_znak = chr(nova_hodnota + ord('a'))
        sifra = sifra + novy_znak
    else:
        #medzery a ine znaky len odpiseme
        sifra = sifra + znak

print("Zašifrovaný text:", sifra)