from fastapi import FastAPI
from Car import Car

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/addCar/")
async def add_car(car: Car):
    car.saveData()
    return {"ID": car.id, "Brand": car.brand, "Model": car.model, "Year": car.year, "Kms": car.kms, "Horsepower": car.hp, "Price": car.price, "Color": car.color, "Doors": car.doors}