from pydantic import BaseModel

class Vehicle(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    kms: int
    hp: int
    price: float
    color: str


    def __str__(self):
        return f"Brand: {self.brand} \n Model: {self.model} \n Year: {self.year} \n Kms: {self.kms} \n Hp: {self.hp} \n Price: {self.price} \n Color: {self.color}"

    def addBrand(self, brand: str):
        self.brand = brand

    def getBrand(self):
        return self.brand

    def addModel(self, model: str):
        self.model = model

    def getModel(self):
        return self.model

    def addYear(self, year: int):
        self.year = year

    def getYear(self):
        return self.year

    def addKms(self, kms: int):
        self.kms = kms

    def getKms(self):
        return f"{self.kms}kms"

    def addHp(self, hp: int):
        self.hp = hp

    def getHP(self):
        return f"{self.hp} Horsepower"

    def addPrice(self, price: float):
        self.price = price

    def getPrice(self):
        return f"{self.price}€"

    def addColor(self, color: str):
        self.color = color

    def getColor(self):
        return self.color

    def increaseKms(self, kms: int):
        self.kms += kms

    def getGenericDescription(self):
        return (f"This vehicle is a/an {self.brand} {self.model} from {self.year} with {self.kms} kms and  {self.hp} hp.\n"
                f"The main color is {self.color} and you can have it for a small amount of {self.price}€.")

