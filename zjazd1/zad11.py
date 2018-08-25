def zwroc_pozycje(x, y):
	if 0 <= x <= 9:
		if 0 <= y <= 9:
			return "Gracz znajduje sie w lewym dolnym rogu."
		elif 9 < y < 91:
			return "Gracz znajduje sie w lewej krawedzii."
		elif 91 <= y <= 100:
			return "Gracz znajduje sie w lewym gornym rogu."
	elif 9 < x < 91:
		if 0 <= y <= 9:
			return "Gracz znajduje sie w dolnej krawedzii."
		elif 9 < y < 91:
			return "Gracz znajduje sie w centrum."
		elif 91 <= y <= 100:
			return "Gracz znajduje sie w gornej krawedzii."
	elif 91 <= x <= 100:
		if 0 <= y <= 9:
			return "Gracz znajduje sie w prawym dolnym rogu."
		elif 9 < y < 91:
			return "Gracz znajduje sie w prawej krawedzii."
		elif 91 <= y <= 100:
			return "Gracz znajduje sie w prawym gornym rogu."

	return "Gracz znajduje sie poza plansza."



print(zwroc_pozycje(95, 95))