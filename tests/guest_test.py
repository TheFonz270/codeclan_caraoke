import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Harry", 50, "Greese Lightning")
    
    def test_guest_has_name(self):
        self.assertEqual("Harry", self.guest1.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)
    
    def test_guest_has_fav_song(self):
        self.assertEqual("Greese Lightning", self.guest1.fav_song)