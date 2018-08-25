min = max = None

while True:
	wpis = input('Podaj liczbe lub zakoncz program (koniec): ')
	if (wpis == 'koniec'):
		break
	liczba = int(wpis)
	try:
		if max is None or liczba > max:
			max = liczba
		if min is None or liczba < min:
			min = liczba
	except:
		print('Prosze podac poprawna wartosc!')

print(f'Minimalna wartosc: {min}')
print(f'Maksymalna wartosc wartosc: {max}')

