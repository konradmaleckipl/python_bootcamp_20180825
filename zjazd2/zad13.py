lista = [x/10 for x in range(0, 11)]
print(lista)

tupla = {(x, x*x, x**6) for x in range(-10, 10)}
print(tupla)

slownik = {x: len(x) for x in ['Kajak', 'xD', 'Test']}
print(slownik)
