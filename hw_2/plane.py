from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo=5, max_cargo=100, weight=15, started=False, fuel=98, fuel_consumption=5):
        super().__init__(weight, started, fuel, fuel_consumption)
        self._cargo = cargo
        self._max_cargo = max_cargo

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if type(value) not in (int, float):
            raise TypeError("Cargo must be int or float number.")
        self._cargo = value

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, value):
        if type(value) not in (int, float):
            raise TypeError("Cargo must be int or float number.")
        self._max_cargo = value

    def load_cargo(self, value):
        print(f"В транспорт загружено {self.cargo} единиц груза.")
        if self.max_cargo >= self.cargo + value:
            self.cargo += value
            return f"Масса груза увеличилась на {value} единиц и теперь составляет {self.cargo} единиц(а/ы)."
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        last_cargo, self.cargo = self.cargo, 0
        return last_cargo
