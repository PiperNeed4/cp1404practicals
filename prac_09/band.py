from musician import Musician

class Band():

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name}"

    def add(self, musician):
        self.musicians.append(musician)


    # def play(self):
    #     for musician in self.musicians:
    #         if not musician:
    #             return f"{musician.name} needs an instrument!"
    #         return f"{musician.name} is playing: {musician.instruments[0]}"