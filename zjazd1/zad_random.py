from zad_random import randint

x = randint(1, 10)
y = randint(1, 10)
print(f'Ile wynosi iloczyn ponizszych liczb:\nx = {x}\ny = {y}\n')

proba = 0

while True:
	proba+=1
	iloczyn = int(input('Podaj iloczyn: '))
	if iloczyn == x*y:
		print(f'Gratulacje! Podales prawidlowa odpowiedz w {proba} probie!')
		break
	else:
		print('Niestety, probuj dalej.\n')