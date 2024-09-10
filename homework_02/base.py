from abc import ABC

from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        elif self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError("Need gasoline, not started!")

    def move(self, distance=0):
        expected_fuel = self.fuel - distance * self.fuel_consumption
        if expected_fuel >= 0:
            self.fuel = expected_fuel
        else:
            raise NotEnoughFuel("Need gasoline, fuel is over!")
