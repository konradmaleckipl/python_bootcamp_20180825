import json
import os.path


def wypisz(file):
    data = odczytaj(file)
    if not data == []:
        for i, osoba in enumerate(data, start=1):
            print(f'- [{i}] {osoba[0]} {osoba[1]} - rok: {osoba[2]}, pensja: {osoba[3]} PLN')
    else:
        print('Baza jest pusta!\nDodaj najpierw pracownika.')
    return data


def odczytaj(file):
    with open(file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = []
    return data


def zapisz(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f)


baza_pracownikow = 'baza.json'
while True:
    action = input('Co chcesz zrobic? [d - dodaj, w - wypisz, u - usun, x - wyjdz]:  ')
    if action == 'd':
        imie = input('Imie: ')
        nazwisko = input('Nazwisko: ')
        rok_urodzenia = int(input('Rok urodzenia: '))
        pensja = float(input('Pensja: '))
        nowy_pracownik = [imie, nazwisko, rok_urodzenia, pensja]

        if os.path.exists(baza_pracownikow):
            odczytaj(baza_pracownikow)
            data.append(nowy_pracownik)
            zapisz(baza_pracownikow, data)
        else:
            data = [nowy_pracownik]
            zapisz(baza_pracownikow, data)

    elif action == 'w':
        wypisz(baza_pracownikow)
    elif action == 'u':
        data = (baza_pracownikow)
        numer = int(input('Podaj numer pracownika do usuniecia: '))
        data.pop(numer-1)
        zapisz(baza_pracownikow, data)
    elif action == 'x':
        break