def formatuj(*napisy, **znaczniki):
    napis =  "\n".join(napisy)
    for k in znaczniki.keys():
        napis = napis.replace("$"+k, str(znaczniki.get(k)))
    return napis




def test_formatuj_napis_bez_znacznikow():
    assert formatuj("Hello World") == "Hello World"

def test_formatuj_wiele_napisow_bez_znacznikow():
    assert formatuj("Hello World", "I am Konrad", "Testujemy") == "Hello World\nI am Konrad\nTestujemy"

def test_formatuj_napis_ze_znacznikiem():
    assert formatuj("koszt $cena PLN", cena=10) == "koszt 10 PLN"

def test_formatuj_wiele_napisow_ze_znacznikiem():
    assert formatuj("koszt $cena PLN", "kwota $cena brutto", cena=10) == "koszt 10 PLN\nkwota 10 brutto"

def test_formatuj_wiele_napisow_z_wieloma_znacznikami():
    assert formatuj("koszt $samochod to $kwota", "naprawa $samochod bedzie kosztowala $koszt_naprawy", samochod="BMW", kwota=60000, koszt_naprawy=10000)