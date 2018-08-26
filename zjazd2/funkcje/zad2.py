

def wiecej_niz(text, ilosc):
    return set(x for x in set(text) if text.count(x) > ilosc)


def test_wiecej_niz_pusty_napis():
    assert wiecej_niz("", 1) == set()

def test_wiecej_niz():
    assert wiecej_niz("ala ma kota a kot ma ale", 3) == {'a', ' '}
    assert wiecej_niz("przykladowe zdanie do testu", 2) == {'e', ' ', 'd'}