import datetime
rok_urodzenia = int(input('Podaj rok urodzenia: '))
wiek = int(datetime.datetime.now().year) - rok_urodzenia
if wiek >= 18:
	print('Jestes pelnoletni')
else:
	print('Nie jestes pelnoletni')
