import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(5, 20)
        self.room2 = Room(10, 30)

        self.guest1 = Guest("Harry", 50, "Greese Lightning")
        self.guest2 = Guest("James", 50, "Disco Inferno")
        self.guest3 = Guest("Yuko", 50, "Love Story")
        self.party1 = [self.guest1, self.guest2, self.guest3]

        self.guest4 = Guest("Ame", 50, "Wolfs Howl")
        self.guest5 = Guest("Byakuya", 1000, "Money Money Money")
        self.guest6 = Guest("Kai", 25, "Life on Mars")
        self.guest7 = Guest("Dabi", 55, "Fire")
        self.guest8 = Guest("Ei", 45, "Danger Danger")
        self.guest9 = Guest("Fuka", 30, "Burn my Dread")
        self.party2 = [self.guest4, self.guest5, self.guest6, self.guest7, self.guest8, self.guest9]

        self.guest10 = Guest("Sad Tony", 4, "Make the World Go Away")
        self.party3 = [self.guest10]
    
        self.song1 = Song("Crazy Train", 200)
        self.song2 = Song("Mr Crowley", 200)
        self.song3 = Song("Disco Inferno", 200)
        self.songlist1 = [self.song1, self.song2, self.song3]

        self.song4 = Song("Wolfs Howl", 200)
        self.song5 = Song("Money Money Money", 200)
        self.song6 = Song("Life on Mars", 200)
        self.song7 = Song("Fire", 200)
        self.song8 = Song("Danger Danger", 200)
        self.song9 = Song("Burn my Dread", 200)
        self.songlist2 = [self.song4, self.song5, self.song6, self.song7, self.song8, self.song9]

    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_room_guests_have_name(self):
        self.assertEqual("Harry", self.guest1.name)
    
    def test_room_guests_have_wallet(self): 
        self.assertEqual(50, self.guest2.wallet)
    
    def test_room_guests_have_fav_song(self):
        self.assertEqual("Disco Inferno", self.guest2.fav_song)
    
    def test_room_songs_have_name(self):
        self.assertEqual("Crazy Train", self.song1.name)

    def test_room_songs_have_runtime(self):
        self.assertEqual(200, self.song3.run_time)

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
    
    def test_check_room_can_fit_party(self):
        self.assertEqual(True, self.room1.check_capacity(self.party1))
    
    def test_check_room_can_fit_party_false(self):
        self.assertEqual(False, self.room1.check_capacity(self.party2))
        
    def test_room_can_take_guests_confirming_capacity_and_entry_fee(self):
        self.room1.guest_checkin(self.party1)
        self.assertEqual(self.party1, self.room1.guest_list)
        self.assertEqual(True, self.room1.check_capacity(self.party1))
        self.assertEqual(15, self.room1.tab)

    def test_room_cant_take_guests_over_capacity(self):
        self.room1.guest_checkin(self.party2)
        self.assertEqual([], self.room1.guest_list)
        self.assertEqual(False, self.room1.check_capacity(self.party2))
        self.assertEqual(0, self.room1.tab)

    def test_room_cant_take_guests_cant_afford_entry(self):
        self.room1.guest_checkin(self.party3)
        self.assertEqual([], self.room1.guest_list)
        self.assertEqual(True, self.room1.check_capacity(self.party3))
        self.assertEqual(0, self.room1.tab)

    def test_room_can_update_tab(self):
        self.room2.guest_checkin(self.party2)
        self.room2.add_songlist(self.songlist1)
        self.room2.add_songlist(self.songlist2)
        self.room2.calculate_tab(self.room2)
        self.assertEqual(self.room2.tab, 45)
