temp_suma = 0

for i in range(7):
	temp_suma += float(input(f'Podaj temperature w dniu {i+1}: '))
	print(f'Suma dotychczasowych temperatur wynosi: {temp_suma/(i+1)}\n')


