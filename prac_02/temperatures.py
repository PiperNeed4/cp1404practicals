"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celsius_to_farenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_farenheit_to_celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_farenheit_to_celsius(fahrenheit):
    celsius = fahrenheit * 5 / 9 - 32
    print(f"Result: {celsius:.2f} C")


def convert_celsius_to_farenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()