liczby = []

while len(liczby) != 10:
    wpis = input(f'Podaj liczbe numer {len(liczby)+1}: ')
    if wpis == 'koniec':
        break
    else:
        liczby.append(float(wpis))

print(f'Srednia wartosc liczb to: {sum(liczby)/len(liczby)}')