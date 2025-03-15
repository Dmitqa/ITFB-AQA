from hw_2.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    def __init__(self, weight=150, started=False, fuel=70, fuel_consumption=12):
        self._weight = weight
        self.started = started
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if type(value) not in (int, float):
            raise TypeError("Weight must be int or float number.")
        self._weight = value

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if type(value) not in (int, float):
            raise TypeError("Fuel must be int or float number.")
        self._fuel = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if type(value) not in (int, float):
            raise TypeError("Fuel consumption must be int or float number.")
        self._fuel_consumption = value

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                return self.started
            else:
                raise LowFuelError
        else:
            raise ValueError("Failed: DID NOT RAISE")

    def move(self, distance):
        if self.started:
            if self.fuel >= self.fuel_consumption * distance:
                self.fuel -= self.fuel_consumption * distance
                return self.fuel
            else:
                raise NotEnoughFuel
        else:
            raise ValueError
