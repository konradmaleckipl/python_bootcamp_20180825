liczby = [5, 2, 1, 4, 3]
print(liczby)

index_min = None
index_max = None

for i in range(len(liczby)):
    if index_max is None or liczby[i] > liczby[index_max]:
        index_max = i
    if index_min is None or liczby[i] < liczby[index_min]:
        index_min = i


liczby[index_min], liczby[index_max] = liczby[index_max], liczby[index_min]
print(liczby)