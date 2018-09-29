""""Napisz program wczytujący listę adresów email z pliku i tworzący
nowy plik z odfiltrowaną zawartością.
Wejściowy plik może zawierać duplikaty adresów, ten sam adres
pisany różną wielkością liter, linie zawierające białe znaki oraz
błędne adresy email (brak znaku @ lub występuje on wiele razy).
Wynikowy plik powinien zawierać unikalne, posortowane, poprawne
adresy email.
Przykład użycia:
$ python clean_emails.py emails.txt cleaned_emails.txt"""


import sys
import os.path

assert len(sys.argv) > 1, 'Prosze podac nazwe pliku wejsciowego'
file_in = sys.argv[1]
assert len(sys.argv) > 2, 'Prosze podac nazwe pliku wyjsciowego'
file_out = sys.argv[2]
assert os.path.isfile(file_in), 'Taki plik nie istnieje'

emails_final = set()
with open(file_in, 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip().count('@') == 1 and line.strip().endswith('.com'):
            emails_final.add(line.strip().lower())

with open(file_out, 'w', encoding='utf-8') as file_out:
    for email in sorted(emails_final):
        print(email)
        file_out.write(f'{email}\n')