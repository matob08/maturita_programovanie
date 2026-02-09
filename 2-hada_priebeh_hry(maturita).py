subor = open('hada.txt', 'r')
subor2 = open('hada_zapis.txt', 'w')

pocet = 0
maximum = 0

def kompresia(s):
    if s == '':
        return ''
    s = s + '.'
    pismeno = s[0]
    pocet_znakov = 1
    vystup = ''
    for znak in s[1:]:
        if znak == pismeno:
            pocet_znakov += 1
        else:
            vystup += '{} {} '.format(pismeno, pocet_znakov)
            pismeno = znak
            pocet_znakov = 1
    return vystup.strip()

for riadok in subor:
    riadok = riadok.strip()
    print(riadok)
    riadok2 = kompresia(riadok)
    subor2.write(riadok2 + '\n')
    if len(riadok) > maximum:
        maximum = len(riadok)
    pocet += 1

print('Pocet hier v subore:', pocet)
print('Pocet krokov v najdlhsej hre:', maximum)

subor.close()
subor2.close()