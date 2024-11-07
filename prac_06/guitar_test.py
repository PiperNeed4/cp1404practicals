"""
Estimate: 10 minutes
Actual: 9 minutes
"""
from prac_06.guitar import Guitar

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2013, 2000)

print(f"{first_guitar.name} get_age() - Expected 100 got {first_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 9 got {another_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True got {first_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False got {another_guitar.is_vintage()}")
