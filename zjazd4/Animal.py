import pytest

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print('knock knock')

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self):
        print('how how')


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self):
        print('... (sorry - that\'s cat!)')




def test_age():
    dog = Dog('Pies', 5)
    cat = Cat('Kot', 2)
    assert dog > cat

def test_animal_sound(capsys):
    animal = Animal('Zwierze', 3)
    animal.sound()
    out = capsys.readouterr()[0]
    assert out == 'knock knock\n'

def test_cat_sound(capsys):
    cat = Cat('Kot', 2)
    cat.sound()
    out = capsys.readouterr()[0]
    assert out == '... (sorry - that\'s cat!)\n'

def test_dog_sound(capsys):
    dog = Dog('Pies', 5)
    dog.sound()
    out = capsys.readouterr()[0]
    assert out == 'how how\n'