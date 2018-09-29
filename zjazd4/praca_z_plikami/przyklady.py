plik = open('pliki_wejsciowe\dane.txt')
print(plik)
plik.close()


with open('pliki_wejsciowe\dane.txt', 'r', encoding='utf-8') as plik:
    print(dir(plik))
    print(plik.read())
    print(plik)
