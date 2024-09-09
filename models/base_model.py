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
    
    def to_dict(self):
         """Returns the key, value pairs of __dict__ of the instance"""
         obj_instance_attr_set = self.__dict__
         obj_instance_attr_set['__class__'] = self.__class__.__name__
         obj_instance_attr_set['created_at'] = self.created_at.isoformat()
         obj_instance_attr_set['updated_at'] = self.updated_at.isoformat()
         return obj_instance_attr_set
    


if __name__ == "__main__":

    model = BaseModel()

    print(model)
    print(model.created_at)
    print(model.updated_at)

    model.save()

    print(f"\n{model}")
    print(model.created_at)
    print(model.updated_at)
    print(f"\n{model.to_dict()}")