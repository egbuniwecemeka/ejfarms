import uuid

class BaseModel:
    """"""
    def __init__(self):
        """"""
        self.id = str(uuid.uuid4())

if __name__ == "__main__":
    model = BaseModel()
    print(model.id)