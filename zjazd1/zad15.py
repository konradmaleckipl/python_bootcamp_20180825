from random import randint

skarb_x = randint(1, 10)
skarb_y = randint(1, 10)
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
roznica_x = 0
roznica_y = 0

min_krokow = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
kroki = 0

print(f'Pozycja skarbu:\n x = {skarb_x}\ny = {skarb_y}')

while True:
    print(f'\nTwoja pozycja:\n x = {gracz_x}\n y = {gracz_y}')

    if skarb_x == gracz_x and skarb_y == gracz_y:
        print('Gratulacje! Odnalazles skarb! Koniec Gry!')
        break

    roznica_x = abs(skarb_x-gracz_x)
    roznica_y = abs(skarb_y-gracz_y)
    txt = input('Podaj kierunek: ')
    kroki+=1
    if txt == 'up':
        gracz_y += 1
    elif txt == 'down':
        gracz_y -= 1
    elif txt == 'left':
        gracz_x -= 1
    elif txt == 'right':
        gracz_x += 1
    elif txt == 'koniec':
        print('Konczysz gre...')
        break

    if  10 < gracz_x < 1 or 10 < gracz_y < 1:
        print('Poza plansza! Koniec gry!')
        break

    if (gracz_x, gracz_y) == (skarb_x, skarb_y):
        print('Gratulacje! Odnalazles skarb! Koniec Gry!')
        break

    if abs(skarb_x-gracz_x) < roznica_x or abs(skarb_y-gracz_y) < roznica_y:
        print('Zblizasz sie do skarbu!')
    else:
        print('Oddalasz sie od skarbu :(')

