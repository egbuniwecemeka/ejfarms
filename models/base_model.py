import uuid
import datetime

class BaseModel:
    def __init__(self):
            """Initializes instance attributes"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


if __name__ == "__main__":

    model = BaseModel()
    model1 = BaseModel()

    print(model.id)
    print(model.created_at)
    print(model.updated_at)
    print(model1)