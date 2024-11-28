from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 18, 2)
my_taxi.drive(40)
print(f"${my_taxi.get_fare()}" )
print(my_taxi.__str__())