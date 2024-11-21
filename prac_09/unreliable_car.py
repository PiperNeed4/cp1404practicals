from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability >= random.randint:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven
