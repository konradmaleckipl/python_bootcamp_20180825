class Product:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self.price = price
        self._vat = 0.23

    @property
    def full_name(self):
        return f'Product: {self._name}'

    @property
    def discount_price(self):
        '''discount price help info :)'''
        return self.price * 0.8

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value

    @property
    def vat(self):
        return self._vat

    @vat.setter
    def vat(self, value):
        if 0.10 < value < 0.30:
            self._vat = value


p1 = Product(1, 'bułka', 10)
print(p1.price)
print(p1._id)
print(p1.full_name)
print(p1.discount_price)

print(p1.name)
p1.name = 'ala ma kota'
print(p1.name)
print(p1._name)
p1.name = 'co'

print(p1.name)
print(p1.vat)
p1.vat = 0.15
print(p1.vat)
help(Product.discount_price)

