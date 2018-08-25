skarbonka = 20

while skarbonka <= 2000:
	print(f'Stan twojej skarbonki: {skarbonka}')
	try:
		wplata = float(input('Podaj kwote do wplaty: '))
		skarbonka += wplata
		print(f'Stan twojej skarbonkipo wplacie: {skarbonka}\n')
	except:
		print("Podaj poprawna wartosc!\n")
