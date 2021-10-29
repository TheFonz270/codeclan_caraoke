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
    
    def test_room_guests_have_wallet(self): 
        self.assertEqual(50, self.guest2.wallet)
    
    def test_room_guests_have_fav_song(self):
        self.assertEqual("Disco Inferno", self.guest2.fav_song)
    
    def test_room_songs_have_name(self):
        self.assertEqual("Crazy Train", self.song1.name)

    def test_room_songs_have_runtime(self):
        self.assertEqual(180, self.song3.run_time)

    def test_room_can_take_guests(self):
        self.room1.guest_checkin(self.party1)
        self.assertEqual(self.party1, self.room1.guest_list)
    
    def test_guests_can_leave_room(self):
        self.room1.guest_checkin(self.party1)
        self.room1.guest_checkout(self.party1)
        self.assertEqual([], self.room1.guest_list)

    def test_room_can_add_songs(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_song(self.song3)
        self.assertEqual(self.room1.play_list, self.songlist1) 

    def test_room_can_take_songlists(self):
        self.room1.add_songlist(self.songlist1)
        self.assertEqual(self.songlist1, self.room1.play_list)
    
    def test_room_can_remove_songs(self):
        self.room1.add_songlist(self.songlist1)
        self.room1.remove_songs(self.song3)
        self.assertEqual([self.song1, self.song2], self.room1.play_list)
    
    def test_room_can_remove_songlists(self):
        self.room1.add_songlist(self.songlist1)
        self.room1.remove_songlist(self.songlist1)
        self.assertEqual(self.room1.play_list, [])
    
    def test_entry_fee_added_to_tab(self):
        self.room1.guest_checkin(self.party1)
        self.assertEqual(15, self.room1.tab)