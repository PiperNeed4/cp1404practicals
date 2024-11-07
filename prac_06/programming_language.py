"""
Estimate: 20 minutes
Actual: 18 minutes

"""


class ProgrammingLanguage:

    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return "Dynamic" in self.typing
