from Stand import Stand
from Vehicle import Vehicle
from Car import Car
from Moto import Moto
from Manager import Manager
from Salesman import Salesman
from Client import Client

CostaCars = Stand("CostaCars", "Rua da Programacao", "919293945")
print(CostaCars)

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

Car1 = Car(1, "BMW", "Serie 1", 2000, 120000, 125, 7000, "Black", 5)
Car2 = Car(2, "Porsche", "Cayman", 2006, 70000, 225, 63000, "white", 5)
Car3 = Car(3, "Honda", "S2000", 2000, 136000, 240, 35000, "gray", 3)
print(Car1)
print(Car2)
print(Car3)

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

Car1HP = Vehicle.getHP(Car1)
Car2Kms = Vehicle.getKms(Car2)
print(Car1HP)
print(Car2Kms)

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

GenDescripCar3 = Vehicle.getGenericDescription(Car3)
print(GenDescripCar3)

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.add_car(Car1)
CostaCars.add_car(Car2)
CostaCars.add_car(Car3)
CostaCars.show_cars()

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.delete_car(1)
CostaCars.show_cars()

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

Moto1 = Moto(4, "Yamaha", "R7", 2015, 70000, 138, 19000, "Blue", "No")
Moto2 = Moto(5, "Honda", "Forza 750", 2007, 185000, 59, 8000, "Black", "Yes")
Moto3 = Moto(6, "Suzuki", "Hayabusa", 2013, 20000, 315, 17000, "Orange", "No")
print(Moto1)
print(Moto2)
print(Moto3)

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.add_moto(Moto1)
CostaCars.add_moto(Moto2)
CostaCars.add_moto(Moto3)
CostaCars.show_motos()

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.delete_moto(5)
CostaCars.show_motos()

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

# Assuming you have some vehicles added to CostaCars.cars or CostaCars.motos
matching_vehicles = CostaCars.search_by_model("Hayabusa")

if matching_vehicles:
    for vehicle in matching_vehicles:
        print(vehicle)  # This will use the __str__ method of the Vehicle class to print details
else:
    print("No vehicles found for the search model.")

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

Manager1 = Manager(1, "João")
Salesman1 = Salesman(2, "Luís Paiva", 5)
Salesman2 = Salesman(3, "Rita Cardoso", 10)
Salesman3 = Salesman(4, "Fábio Poças", 15)
Client1 = Client(5, "José Silva", 7)
Client2 = Client(6, "Andreia Mota", 4)
Client3 = Client(7, "António Pereira", 2)

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.add_user(Manager1)
CostaCars.add_user(Salesman1)
CostaCars.add_user(Salesman2)
CostaCars.add_user(Salesman3)
CostaCars.add_user(Client1)
CostaCars.add_user(Client2)
CostaCars.add_user(Client3)
CostaCars.show_users()

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.delete_user(6)
CostaCars.show_users()

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.search_user_by_type("Client")

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

CostaCars.search_user_by_type("Cliente")

print("\n")
print("##" * 10)
print("##" * 10)
print("\n")

Car1.increaseKms(10)
print(Car1)