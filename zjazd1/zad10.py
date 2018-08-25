liczba_1 = int(input('Podaj pierwsza liczbe: '))
liczba_2 = int(input('Podaj druga liczbe: '))
operacja = input('Podaj rodzaj operacji: ')
wynik = None

if operacja == '+':
	wynik = liczba_1+liczba_2
elif operacja == '-':
	wynik = liczba_1-liczba_2
elif operacja == '*':
	wynik = liczba_1*liczba_2
elif operacja == '/':
	wynik = liczba_1/liczba_2
elif operacja == '%':
	wynik = liczba_1%liczba_2

	
if wynik is not None:
	print('Wynik:', wynik)
else:
	print('Nieznany typ operatora!')