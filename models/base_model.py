import uuid
import datetime

class BaseModel:
    """A base class for all common attributes/methods for other classes"""
    def __init__(self):
            """Initializes public instance attributes"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def save(self):
         """Updates current datetime anytime an object is changed"""
         self.updated_at = datetime.datetime.now()
    
    def __str__(self):
         """Returns a string representation of BaseModel instance"""
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


if __name__ == "__main__":

    model = BaseModel()

    print(model)
    print(model.id)