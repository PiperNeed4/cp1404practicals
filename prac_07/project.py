import datetime

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):

        self.name = name
        self.start_date = start_date
        # self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = cost_estimate
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name} {self.start_date} {self.priority} {self.cost_estimate} {self.completion_percentage}"

    def __lt__(self, other):
        return self.start_date < other.start_date

    def is_complete(self):
        return self.completion_percentage == 100