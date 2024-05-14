from Vehicle import Vehicle
from pydantic import BaseModel


class Car(Vehicle, BaseModel):
    doors: int

    def __str__(self):
        return f"{super().__str__()} \n Doors: {self.doors}"

    def saveData(self):
        print("Car added successfuly!")