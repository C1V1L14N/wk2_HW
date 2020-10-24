import unittest
from classes.song import *
from classes.room import *

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
    def test_add_song(self):
        song = Song("Tainted Love", "Soft Cell", 2.34, "pop", False)
        self.song.add_song(song)
        self.assertEqual(1, len(self.song.playlist))

    def test_find_song__with_result(self):
        self.song.add_song(self.song)
        self.assertEqual(True, self.song.find_song("Believe"))

    def test_find_song__without_result(self):
        self.song.add_song(self.song)
        self.assertEqual(False, self.song.find_song("Country House"))

    def test_remove_song(self):
        self.song.add_song(self.song)
        self.song.remove_song("Believe")
        self.assertEqual(0, len(self.song.playlist))

    def test_remove_song__not_found(self):
        self.song.add_song(self.song)
        self.song.remove_song("Country House")
        self.assertEqual(1, len(self.song.playlist))  
