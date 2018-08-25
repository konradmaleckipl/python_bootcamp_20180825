
suma = 0

while True:
    wpis = input('Podaj liczbe: ')
    if wpis == 'koniec':
        break
    try:
        suma += int(wpis)
    except:
        print('Prosze podac poprawa liczbe!')

print(f'Suma wynosi: {suma}')