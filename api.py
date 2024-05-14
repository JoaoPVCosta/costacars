from fastapi import FastAPI
from Car import Car
from Moto import Moto

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/addCar/")
async def add_car(car: Car):
    car.saveData()
    return {"ID": car.id, "Brand": car.brand, "Model": car.model, "Year": car.year, "Kms": car.kms, "Horsepower": car.hp, "Price": car.price, "Color": car.color, "Doors": car.doors}

@app.post("/addMoto/")
async def add_moto(moto: Moto):
    moto.saveData()
    return {"ID": moto.id, "Brand": moto.brand, "Model": moto.model, "Year": moto.year, "Kms": moto.kms, "Horsepower": moto.hp, "Price": moto.price, "Color": moto.color, "Sidecar": moto.sidecar}