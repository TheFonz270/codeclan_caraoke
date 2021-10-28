import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(10)

        self.guest1 = Guest("Harry", 50, "Greese Lightning")
        self.guest2 = Guest("James", 50, "Disco Inferno")
        self.guest3 = Guest("Yuko", 50, "Love Story")
        self.party1 = [self.guest1, self.guest2, self.guest3]
    
        self.song1 = Song("Crazy Train", 200)
        self.song2 = Song("Mr Crowley", 160)
        self.song3 = Song("Disco Inferno", 180)
        self.songlist1 = [self.song1, self.song2, self.song3]
    
    def test_room_has_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    def test_room_guests_have_name(self):
        self.assertEqual("Harry", self.guest1.name)
    

    