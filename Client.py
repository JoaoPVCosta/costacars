from costacars.Users import User
from costacars.TypeUserEnum import TypeUserEnum

class Client(User):
    def __init__(self, user_id, name, discount: int):
        super().__init__(user_id, name)
        self.discount = discount
        self.type = TypeUserEnum.Client