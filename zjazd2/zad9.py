cennik = {
    'Banan': 3.50,
    'Jablko': 2.30,
    'Limonka': 4.70
}
for k in cennik.keys():
    print(k+": "+str(cennik[k])+"   ", end='')
nazwa = input('\nPodaj nazwe produktu: ')
waga = float(input('Podaj wage: '))

print(f'Kwota do zaplaty: {cennik[nazwa]*waga} PLN')