import unittest
import uuid
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_is_uuid(self):
        """Assert that the uuid of two instances are not equal"""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)

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
    
    def test_created_at_is_instance(self):
        """Assert created_at is instance of datetime"""
        model = BaseModel()

        self.assertIsInstance(model.created_at, datetime.datetime)

    def test_updated_at_is_instance(self):
        """Assert updated_at is instance of datetime"""
        model = BaseModel()

        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_updated_at_equals_created_at(self):
        """Assert updated_at equals created_at"""
        model = BaseModel()

        self.assertEqual(model.updated_at, model.created_at)

    def test_save_update_at(self):
        """Assert save method updates update_at"""
        model = BaseModel()
        original_update_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, original_update_at)


if __name__ == "__main__":
    unittest.main()