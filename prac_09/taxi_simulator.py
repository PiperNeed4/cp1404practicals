from inspect import isclass

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    print("Let's drive!")
    user_choice = input(MENU).lower()
    while user_choice != "q":
        if user_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare}")
                bill_to_date += fare
                print(f"Bill to date: ${bill_to_date}")
        else:
            print("Invalid option")
        user_choice = input(MENU).lower()
    print(f"Total trip cost: ${bill_to_date}")
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi.__str__()}")


def choose_taxi(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi.__str__()}")
    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice < 0 or taxi_choice > len(taxis) - 1:
        print("Invalid taxi choice")
        taxi_choice = int(input("Choose taxi: "))
    return taxis[taxi_choice]



main()
