"""
Estimate: 40 minutes
Actual:
"""
from prac_01.temperatures import choice

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ileter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")

def main():
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
            choice = input(MENU).upper()