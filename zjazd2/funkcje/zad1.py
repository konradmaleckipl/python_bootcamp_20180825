def czy_jest_pierwsza(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(czy_jest_pierwsza(5))


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(7)

def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert not czy_jest_pierwsza(6)