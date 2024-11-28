from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialized car class with reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car object."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive only if reliability is greater or equal to a random integer between 1 and 100."""
        if self.reliability >= randint(1, 100):
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven
