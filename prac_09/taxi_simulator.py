from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>>"
current_taxi = None
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")
user_choice = input(MENU).lower()
while user_choice != "q":
    if user_choice == "c":
        taxi = choose_taxi()
    elif user_choice == "d":
        drive()

def choose_taxi():
    pass

def drive():
    pass