lista = []

while True:
	wpis = input('Podaj liczbe lub zakoncz program (exit): ')
	if (wpis == 'exit'):
		break
	lista.append(float(wpis))

print('\nMinimalna wartosc:', min(lista))
print('Maksymalna wartosc wartosc:', max(lista))






