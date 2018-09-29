import json



obj1 = ['AAA', 2, 3, ['Konrad', 'Magda']]

print(json.dumps(obj1))
print(type(json.dumps(obj1)))

#zapis do pliku
with open('example.json', 'w', encoding='utf-8') as f:
    json.dump(obj1, f)

#otwarcie pliku
with open('example.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(type(data))

data.append('cos tam')
print(data)

with open('example.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)