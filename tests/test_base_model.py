import unittest
import uuid
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_is_uuid(self):
        """Assert that the uuid of two instances are not equal"""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertEqual(model1.id, model2.id)

    def test_id_is_string(self):
        """Assert that instance is a string"""
        model = BaseModel()

        self.assertIsInstance(model.id, str)
    
    def test_is_uuid(self):
        """Assert the ID is a unique UUID"""
        model = BaseModel()

        try:
            uuid.UUID(model.id)
        except ValueError:
            self.fail("The UUID is not valid!")
    

    if __name__ == "__main__":
        unittest.main()