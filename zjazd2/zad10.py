dict = {}
napis = input('Podaj napis: ')
for x in napis:
    # if x.lower() not in dict.keys():
    #     dict[x.lower()] = 1
    # else:
    #     dict[x.lower()]+=1
    dict[x] = dict.get(x, 0)+1

for k in dict.keys():
    print('\"{litera}\"  --->  {ilosc}'.format(litera=k, ilosc=dict[k]))