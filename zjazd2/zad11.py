liczby = set()
while True:
    wpis = input('Podaj liczbe: ')
    if wpis == 'koniec':
        break
    else:
        liczby.add(int(wpis))

licznik = sum(1 for x in liczby if 0 < x <= 100 and x % 2 ==0)

print(f'Ilosc liczb unikalnych: {len(liczby)}')
print(f'Ilosc liczb parzystych z przedzialu 0-100: {licznik}')