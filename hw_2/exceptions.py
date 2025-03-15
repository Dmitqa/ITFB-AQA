class LowFuelError(Exception):
    def __init__(self, message="Fuel value = 0."):
        self.message = message
        super().__init__(self.message)


class NotEnoughFuel(Exception):
    def __init__(self, message="Fuel not enough."):
        self.message = message
        super().__init__(self.message)


class CargoOverload(Exception):
    def __init__(self, message="Overload! Remove extra weight."):
        self.message = message
        super().__init__(self.message)
