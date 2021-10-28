import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Crazy Train", 200)
    
    def test_song_has_name(self):
        self.assertEqual("Crazy Train", self.song1.name)
    
    def test_song_has_run_time(self):
        self.assertEqual(200, self.song1.run_time)