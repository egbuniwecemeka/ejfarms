import uuid

class BaseModel:
    def __init__(self):
            """Initializes instance attributes"""
            self.id = str(uuid.uuid4())

model = BaseModel().id
print(model)