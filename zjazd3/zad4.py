import pytest

class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt "{self.nazwa}", id: {self.id}, cena: {self.cena} PLN')

    def __str__(self):
        return 'Product: {id: {id}, nazwa: {nazwa}, cena: {cena}}'.format(id=self.id, nazwa=self.nazwa, cena=self.cena)


class Basket:
    def __init__(self):
        self.koszyk = {}

    def add_product(self, product, amount):
        if product not in self.koszyk:
            self.koszyk[product] = amount
        else:
            x = self.koszyk[product]
            self.koszyk[product] = x+amount

    def count_total_price(self):
        sum = 0
        for product in self.koszyk.keys():
            sum += product.cena * self.koszyk[product]
        return sum

    def generate_report(self):
        output_text = 'Produkty w koszyku:\n'
        for product in self.koszyk.keys():
            output_text += f'- {product.nazwa} ({product.id}), cena: {product.cena} x {self.koszyk[product]}\n'
        output_text += f'W sumie: {self.count_total_price()}'
        print(output_text)


def test_product_str_print():
    product = Product(1, 'Woda', 10.00)
    #print(product)


def test_count_total_price():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50.0

def test_count_total_price_multiple_products():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50.0
    product2 = Product(2, 'Kawa', 20.0)
    basket.add_product(product2, 2)
    assert basket.count_total_price() == 90

def test_generate_report(capsys):
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    basket.generate_report()
    out = capsys.readouterr()[0]
    assert out == 'Produkty w koszyku:\n- Woda (1), cena: 10.0 x 5\nW sumie: 50.0\n'

def test_generate_report_multiple_products(capsys):
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    basket.generate_report()
    out = capsys.readouterr()[0]
    assert out == 'Produkty w koszyku:\n- Woda (1), cena: 10.0 x 5\nW sumie: 50.0\n'
    product2 = Product(2, 'Kawa', 20.0)
    basket.add_product(product2, 2)
    basket.generate_report()
    out = capsys.readouterr()[0]
    assert out == 'Produkty w koszyku:\n- Woda (1), cena: 10.0 x 5\n- Kawa (2), cena: 20.0 x 2\nW sumie: 90.0\n'