"""
    A simple class module meant to understand class attributes and methods better
"""

class Car:
    """A Car type class"""

    wheels = 4  #class attribute/variable (class level not instance level)

    @classmethod
    def modify_wheels(cls, new_wheels):
        cls.wheels = new_wheels
        return cls.wheels

wheels_no = Car.modify_wheels(6)
print(wheels_no)