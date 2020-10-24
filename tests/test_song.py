import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Believe", "Cher", 3.59, "pop", False)

    def test_song_has_title(self):
        self.assertEqual("Believe", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Cher", self.song.artist)

    def test_song_has_duration(self):
        self.assertEqual(3.59, self.song.duration)

    def test_song_has_genre(self):
        self.assertEqual("pop", self.song.genre)

    def test_song_has_explicit(self):
        self.assertEqual(False, self.song.explicit)

# test_create_song

