napis = input('Podaj napis:')
ilosc = 0

nawias_start = napis.index('<')
nawias_end = napis.index('>')-1
print(f'Ilosc znakow w nawiasie: {nawias_end-nawias_start}')

7