import uuid

class BaseModel:
    """"""
    def __init__(self):
        """"""
        self.id = str(uuid.uuid4())
        

if __name__ == "__main__":
    model1 = BaseModel()
    model2 = BaseModel()
    print(model1.id)
    print(model2.id)