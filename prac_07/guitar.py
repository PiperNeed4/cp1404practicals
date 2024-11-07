class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        return self.get_age() > 50

    def __lt__(self, other):
        return self.year < other.year