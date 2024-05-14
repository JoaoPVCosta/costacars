from Car import Car
from Moto import Moto
from costacars.Users import User


class Stand:

    def __init__(self, name, address, cell):
        self.name = name
        self.address = address
        self.cell = cell
        self.cars = []
        self.motos = []
        self.users = []

    def __str__(self):
        return f"Stand Name: {self.name}\nAddress: {self.address}\nCell: {self.cell}"
    #Este método passa a retornar os dados de forma organizada.

    def add_car(self, car: Car):
        self.cars.append(car)

    def show_cars(self) -> list:
        print(f"Cars:\n ----")
        for c in self.cars:
            print(f"ID: {c.id}, Brand: {c.brand}, Model: {c.model}\n"
                  f"Year: {c.year}, Kms: {c.kms}, Horsepower: {c.hp}\n"
                  f"Price: {c.price}€, Doors: {c.doors}\n ----------")
        return self.cars

    def delete_car(self, car_id: int):
        for c in self.cars:
            if c.id == car_id:
                self.cars.remove(c)
                break

    def add_moto(self, moto: Moto):
        self.motos.append(moto)

    def show_motos(self) -> list:
        print(f"Motos:\n ----")
        for c in self.motos:
            print(f"ID: {c.id}, Brand: {c.brand}, Model: {c.model}\n"
                  f"Year: {c.year}, Kms: {c.kms}, Horsepower: {c.hp}\n"
                  f"Price: {c.price}€, Sidecar: {c.sidecar}\n ----------")
        return self.motos

    def delete_moto(self, moto_id: int):
        for c in self.motos:
            if c.id == moto_id:
                self.motos.remove(c)
                break

    def search_by_model(self, model: str) -> list:
        """
        This method searches for vehicles in the stand based on the provided model.

        Args:
            model: The model name to search for (case-insensitive).

        Returns:
            A list of Vehicle objects that match the search criteria.
        """
        matching_vehicles = []
        for vehicle in self.cars + self.motos:  # Combine cars and motorcycles
            if model.lower() in vehicle.getModel().lower():  # Case-insensitive search
                matching_vehicles.append(vehicle)
        return matching_vehicles

    def add_user(self, user: User):
        self.users.append(user)

    def show_users(self):
        for u in self.users:
            print(f"ID: {u.user_id}, Name: {u.name}, Type: {u.type.value}\n"
                  f"-----")
        return self.users

    def delete_user(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                break

    def search_user_by_type(self, type_user: str):
        results = []
        for u in self.users:
            if u.type.value == type_user:
                print(f"ID: {u.user_id} \n"
                      f"Name: {u.name}\n"
                      f"Type: {u.type.value}\n"
                      f"-----")
                results.append(u)
        if results:
            return results
        else:
            print("Não existe esse tipo de cliente.")