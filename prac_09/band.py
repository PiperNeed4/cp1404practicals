from musician import Musician


class Band:
    """Represent a band object."""

    def __init__(self, name):
        """Initialize a band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band object."""
        return f"{self.name} {[musician.__str__() for musician in self.musicians]}"

    def add(self, musician):
        """Add a musician to the musicians list."""
        self.musicians.append(musician)

    def play(self):
        """Lists musicians and their instruments."""
        for musician in self.musicians:
            print(musician.play())
