from fileinput import close

from prac_03.capitalist_conrad import out_file
from prac_07.guitar import Guitar


def main():
    in_file = open("guitars.csv", 'r')
    guitars = []
    for line in in_file:
        parts = line.strip().split(',')
        # guitars.append(parts)
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    display_guitars(guitars)
    in_file.close()
    out_file = open("guitars.csv", 'w')
    for guitar in guitars:
        print(guitar, sep="", file=out_file)


def display_guitars(guitars):
    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost}{vintage_string}")


main()
