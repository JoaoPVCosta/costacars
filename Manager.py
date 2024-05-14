from Users import User
from TypeUserEnum import TypeUserEnum

class Manager(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.type = TypeUserEnum.Manager