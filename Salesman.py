from costacars.Users import User
from costacars.TypeUserEnum import TypeUserEnum

class Salesman(User):
    def __init__(self, user_id, name, comission: int):
        super().__init__(user_id, name)
        self.comission = comission
        self.type = TypeUserEnum.Salesman