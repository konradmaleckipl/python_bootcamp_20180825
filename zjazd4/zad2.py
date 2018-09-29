import sys
import os.path


assert len(sys.argv) > 1, 'Prosze podac nazwe pliku'
plik = sys.argv[1]
assert os.path.isfile(plik), 'Taki plik nie istnieje'

user_total_time = {}
with open(plik, 'r', encoding='utf-8') as file:
    # for i, linia in enumerate(file.read().splitlines(), start=1):
    #     print(f'{i}: {linia}')
    user_last_login = {}
    for line in file:
        user_id, action, time_str = line.split(';')
        time = int(time_str)
        if action == 'LOGIN':
            user_last_login[user_id] = time
        elif action == 'LOGOUT':
            user_total_time[user_id] = user_total_time.get(user_id, 0) + time - user_last_login[user_id]

for item in sorted(user_total_time.items(), key=lambda x: x[1]):
    print(f'{item[0]}: {item[1]} s')










