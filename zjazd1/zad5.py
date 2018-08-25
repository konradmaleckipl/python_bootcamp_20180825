miasto_a = input('Podaj nazwe miasta A: ')
miasto_b = input('Podaj nazwe miasta B: ')
dystans = float(input('Podaj ilosc kilometrow: '))
cena_paliwa = float(input('Poda cene paliwa: '))
spalanie = float(input('Podaj spalanie na 100km: '))
koszt_przejazdu = dystans/100*spalanie*cena_paliwa

print(f'\nMiasto A: {miasto_a}')
print(f'Miasto B: {miasto_b}')
print(f'Dystans {miasto_a}-{miasto_b}: {dystans}')
print(f'Cena paliwa: {cena_paliwa}')
print(f'Spalanie na 100km: {spalanie}\n')
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {koszt_przejazdu:.2f} PLN')