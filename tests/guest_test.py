import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def set_up(self):
        self.customer1("Harry", 50, "Greese Lightning")
    
    def test_guest_has_name(self):
        self.assertEqual("Harry", self.guest1.name)