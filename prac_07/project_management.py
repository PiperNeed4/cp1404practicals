"""
Estimate: 40 minutes
Actual: 174 minutes
"""
from prac_07.project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit\n >>> ")


def main():
    projects = []
    in_file = open("projects.txt", 'r', encoding="utf-8-sig")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('  ')
        print(parts)
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    print(projects)
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            load_project(projects)
            choice = input(MENU).upper()
        elif choice == "S":
            save_project(projects)
            choice = input(MENU).upper()
        elif choice == "D":
            display_project(projects)
            choice = input(MENU).upper()
        elif choice == "F":
            filter_project(projects)
            choice = input(MENU).upper()
        elif choice == "A":
            add_project(projects)
            choice = input(MENU).upper()
        elif choice == "U":
            update_project(projects)
            choice = input(MENU).upper()
        else:
            print("Invalid input")
            choice = input(MENU).upper()
    save_choice = input("Would you like to save to projects.txt? ").upper()
    if save_choice == "Y":
        filename = input("Enter file name: ")
        out_file = open(filename, 'w')
        for project in projects:
            print(project, sep="", file=out_file)
    print("Thank you for using custom-built project management software.")


def load_project(projects):
    filename = input("Enter file name: ")
    in_file = open(filename, 'r', encoding="utf-8-sig")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('  ')
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))


def save_project(projects):
    filename = input("Enter file name: ")
    out_file = open(filename, 'w')
    for project in projects:
        print(project, sep="", file=out_file)


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def display_project(projects):
    print("test")
    projects.sort()
    print("Incomplete projects:")
    for i, project in enumerate(projects, 1):
        if not project.is_complete():
            print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, "
                  f"estimate: {project.cost_estimate}, completion: {project.completion_percentage}%")
    print("Complete projects:")
    for i, project in enumerate(projects, 1):
        if project.is_complete():
            print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, "
                  f"estimate: {project.cost_estimate}, completion: {project.completion_percentage}%")


def filter_project(projects):
    filter_date = input("Show projects that start after date (dd/mm/yy)")
    converted_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    for i, project in enumerate(projects, 1):
        if project.start_date > converted_date:
            print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, "
                  f"estimate: {project.cost_estimate}, completion: {project.completion_percentage}%")


def update_project(projects):
    for i, project in enumerate(projects, 1):
        print(f"{i - 1} {project.name}, start: {project.start_date}, priority: {project.priority}, "
              f"estimate: {project.cost_estimate}, completion: {project.completion_percentage}")
    project_choice = int(input("Project choice: "))
    for projects[project_choice] in projects:
        print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, "
              f"estimate: {project.cost_estimate}, completion: {project.completion_percentage}")
    new_percentage = int(input("New percentage: "))


main()
