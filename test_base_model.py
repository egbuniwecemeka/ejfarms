#!/usr/bin/python3
from models.base_model import BaseModel

model = BaseModel()

model.name = "My First Model"
model.my_number = 89
model.age = 29

print(model)