#!/usr/bin/python3
from models.base_model import BaseModel

model = BaseModel()

model.name = "My First Model"
model.my_number = 89
model.age = 29

print(model)
model.save()
print(f"\n{model}")
my_model_json = model.to_dict()
print(f"\n{my_model_json}")
print("JSON of my model:")
for key in my_model_json.keys():
    print(f"\t{key}: {type(my_model_json[key])} - {my_model_json[key]}")