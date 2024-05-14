from Vehicle import Vehicle
from pydantic import BaseModel


class Moto(Vehicle, BaseModel):
    sidecar: str

    def __str__(self):
        return f"{super().__str__()} \n Sidecar: {self.sidecar}"

    def saveData(self):
        print("Moto added successfuly!")