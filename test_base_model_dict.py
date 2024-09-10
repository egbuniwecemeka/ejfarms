#!/ussr/bin/python3
"""Create BaseModel from dictionary"""

from models.base_model import BaseModel

model = BaseModel()
model.name = "My First Model"
model.my_number = 2
print(model.id)
print(model)
print(type(model.created_at))
print("--")
my_model_json = model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print(f"\t{key}: {(type(my_model_json[key]))} - {my_model_json[key]}")
print("--")
new_model = BaseModel(**my_model_json)
print(new_model.id)
print(new_model)
print(type(new_model.created_at))
print("--")
print(model is new_model)