liczby = [1, -3, 45, -34, 95, -345, -98, -222, 962]
print('Dodanie liczby: {ilosc_dodatnich}'.format(ilosc_dodatnich=sum(1 for x in liczby if x > 0)))
print('Ujemne liczby: {ilosc_ujemnych}'.format(ilosc_ujemnych=sum(1 for x in liczby if x < 0)))