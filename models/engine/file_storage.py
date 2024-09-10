import json
import os

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __object dctionary"""
        return self.__objects
    
    def new(self, obj):
        """sets the key, value of __objects dictionary with obj key id/obj"""
        if obj is not None:
            key = f"{self.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file at __file_path"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            # this assumes object has to_dict method already
            obj_dict[key] = obj.to_dict() 
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)
        
    def reload(self):
        """deserializes JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return

        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, id_ = key.split('.')
                # get class name dynamically from class_name
                cls = globals().get(class_name)
                if cls:
                    self.__objects[key] = cls(**value)
                else:
                    print(f"Warning: Class {class_name} does not exist")
        except json.JSONDecodeError as e:
            print(f"Error decoding json file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")