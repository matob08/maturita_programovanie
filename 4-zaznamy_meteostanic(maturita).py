subor=open("Maturita/meteo_stanice.txt","r",encoding="utf-8")
pocet=0
priemer=0
teplota=''
sum=0

najvacsie=-float('inf')
stanice=[]
max_stanice = ""

for riadok in subor:
    pocet+=1
    
    riadok=riadok.strip()
    
    if '+'in riadok:
        i=riadok.index('+')
    elif '-'in riadok:
        i=riadok.index('-')
    teplota=riadok[i:i+5].strip()
    stanice=riadok[0:3].strip()
    teplota_val = float(teplota.replace(',','.'))
    sum+=teplota_val
    
    if teplota_val > najvacsie:
        najvacsie = teplota_val
        max_stanice = stanice

    print('teplota :',teplota)
    
    
    print('stanice: ',stanice)
print('najvacsie: ',najvacsie)
print('stanice s najvacsou teplotou: ', max_stanice)
print('pocet meteostanic: ',pocet)
subor.close()

def priemerna():
    global teplota, priemer,sum
    if teplota:
        priemer = sum / pocet
    else:
        priemer = 0
    print('priemer: ',priemer)




priemerna()