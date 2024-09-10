"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class BaseMyException(Exception):
    pass


class LowFuelError(BaseMyException):
    pass


class NotEnoughFuel(BaseMyException):
    pass


class CargoOverload(BaseMyException):
    pass
