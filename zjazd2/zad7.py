napis = input('Podaj napis:')
ilosc = 0
samogloski = ['a', 'i', 'e', 'o', 'u', 'y']
for x in napis:
    if x.lower() in samogloski:
        ilosc+=1

print(f'Ilosc wystapien samoglosek w podanym napisie: {ilosc}')