
class ElectricCar:

    def __init__(self, range):
        self.range = range
        self.max_range = range

    def drive(self, distance):
        if distance < self.range:
            distance_traveled = distance
            self.range = self.range - distance
        else:
            distance_traveled = self.range
            self.range = 0
        return distance_traveled

    def charge(self):
        self.range = self.max_range


def test_drive():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
