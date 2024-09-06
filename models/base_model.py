import uuid

class BaseModel:
    def __init__(self):
            """Initializes instance attributes"""
            self.id = str(uuid.uuid4())


model = BaseModel().id
model1 = BaseModel().id

print(model)
print(model1)