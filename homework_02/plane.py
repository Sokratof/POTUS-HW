"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, add_weight):
        if self.max_cargo < self.cargo + add_weight:
            raise CargoOverload("Weight is great!")
        else:
            self.cargo = self.cargo + add_weight
        return self.cargo - add_weight

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

