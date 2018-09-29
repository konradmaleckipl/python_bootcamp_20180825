import csv
import time

with open('WA_Sales_Products_2012-14.csv', 'r', encoding='utf-8') as f:
    years_values = {}
    csv_reader = csv.reader(f, delimiter=',')
    for i, row in enumerate(csv_reader, start=1):
        print(row)
        if i == 1:
            continue
        years_values[row[6]] = years_values.get(row[6], {'quanity': [], 'gross_margin': []})
        if row[9] != '':
            years_values.get(row[6]).get('quanity').append(float(row[9]))
        if row[10] != '':
            years_values.get(row[6]).get('gross_margin').append(float(row[10]))


print('')
total_avg_quanity = 0
total_avg_gross_margin = 0
total_min_quanity = None
total_max_quanity = None
total_min_gross_margin = None
total_max_gross_margin = None
for year, values_dict in years_values.items():
    min_quanity = min(values_dict['quanity'])
    max_quanity = max(values_dict['quanity'])
    min_gross_margin = min(values_dict['gross_margin'])
    max_gross_margin = max(values_dict['gross_margin'])
    avg_quanity = sum(x for x in values_dict['quanity']) / len(values_dict['quanity'])
    avg_gross_margin = sum(x for x in values_dict['gross_margin']) / len(values_dict['gross_margin'])

    total_avg_quanity += avg_quanity
    total_avg_gross_margin += avg_gross_margin
    if total_min_quanity is None:
        total_min_quanity = min_quanity
        total_max_quanity = max_quanity
        total_min_gross_margin = min_gross_margin
        total_max_gross_margin = max_gross_margin
    else:
        if min_quanity < total_min_quanity:
            total_min_quanity = min_quanity
        if max_quanity > total_avg_quanity:
            total_max_quanity = max_quanity
        if min_gross_margin < total_min_gross_margin:
            total_min_gross_margin = min_gross_margin
        if max_gross_margin > total_max_gross_margin:
            total_max_gross_margin = max_gross_margin
    print(f"\nStatystyki dla roku {year}: ")
    print(f"\t- Srednia quanity: {avg_quanity / len(values_dict['quanity'])}")
    print(f"\t- Srednia gross margin: {avg_gross_margin / len(values_dict['gross_margin'])}")
    print(f"\t- Minimalna wartos quanity: {min_quanity}")
    print(f"\t- Maksymalna wartos quanity: {max_quanity}")
    print(f"\t- Minimalna wartos gross margin: {min_gross_margin}")
    print(f"\t- Maksymalna wartos gross margin: {max_gross_margin}")

print('\n')
print(f"Srednia quanity dla wszystkich lat: {total_avg_quanity / len(years_values.keys())}")
print(f"Srednia gross margin dla wszystkich lat: {total_avg_gross_margin / len(years_values.keys())}")
print(f"Minimalna wartos quanity dla wszystkich lat: {total_min_quanity}")
print(f"Maksymalna wartos quanity dla wszystkich lat: {total_max_quanity}")
print(f"Minimalna wartos gross margin dla wszystkich lat: {total_min_gross_margin}")
print(f"Maksymalna wartos gross margin dla wszystkich lat: {total_max_gross_margin}")
