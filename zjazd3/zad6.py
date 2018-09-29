import pytest
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other):
        return Vector(x=self.x * other, y=self.y * other)

    def __eq__(self, other):
        if self.length == other.length:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.length != other.length:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.length > other.length:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.length >= other.length:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.length < other.length:
            return True
        else:
            return False

    def __le__(self, other):
        if self.length <= other.length:
            return True
        else:
            return False

    def __str__(self):
        return f'Vector: (x={self.x}, y={self.y})'


def test_vector_create():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    assert vector_1.x == 1
    assert vector_2.y == 2

def test_vector_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 2
    assert vector_3.y == 4

def test_vector_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == 0
    assert vector_3.y == 0

def test_vector_mul():
    vector_1 = Vector(x=1, y=2)
    vector_2 = vector_1 * 4
    assert vector_2.x == 4
    assert vector_2.y == 8

def test_vector_length():
    vector_1 = Vector(x=3, y=4)
    assert vector_1.length == 5

def test_vector_eq():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=3, y=4)
    assert vector_1 == vector_2

def test_vector_ne():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=2, y=4)
    assert vector_1 != vector_2

def test_vector_gt():
    vector_1 = Vector(x=3, y=4)
    vector_2 = Vector(x=2, y=4)
    assert vector_1 > vector_2

def test_vector_ge():
    vector_1 = Vector(x=2, y=4)
    vector_2 = Vector(x=2, y=4)
    assert vector_1 >= vector_2

def test_vector_lt():
    vector_1 = Vector(x=3, y=3)
    vector_2 = Vector(x=2, y=4)
    assert vector_1 < vector_2

def test_vector_le():
    vector_1 = Vector(x=2, y=4)
    vector_2 = Vector(x=2, y=4)
    assert vector_1 <= vector_2

def test_vector_str(capsys):
    vector_1 = Vector(x=1, y=2)
    print(vector_1)
    out = capsys.readouterr()[0]
    assert out == 'Vector: (x=1, y=2)\n'

def test_vector_sort():
    v1 = Vector(1, 2)
    v2 = Vector(0,1)
    v3 = Vector(3,2)
    v4 = Vector(0,1)
    lista = [v1,v2,v3,v4]
    assert sorted(lista) == [v4, v2, v1, v3]
    assert sorted(lista) == [v2, v4, v1, v3]
    print(lista)