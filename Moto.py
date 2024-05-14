from Vehicle import Vehicle


class Moto(Vehicle):
    sidecar: str

    def __str__(self):
        return f"{super().__str__()} \n Sidecar: {self.sidecar}"