from prac_09.car import Car
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes flagfall and fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a Silver service taxi instance with fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string similar to the taxi class with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the fare modified by the flagfall"""
        return self.flagfall + super().get_fare()
