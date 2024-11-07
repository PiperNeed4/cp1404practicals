"""
Estimate: 40 minutes
Actual:
current: 27
"""
from prac_07.project import Project

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ileter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")

def main():
    projects = []
    in_file = open("projects.txt", 'r', encoding="utf-8-sig")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('  ')
        print(parts)
        # projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    print(projects)
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

def display_projects():
    pass


main()