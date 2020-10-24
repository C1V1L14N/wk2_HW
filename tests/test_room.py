import unittest

from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("fun_room", 16, 500)

    def test_room_has_name(self):
        self.assertEqual("fun_room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(16, self.room.capacity)

    def test_room_has_price(self):
        self.assertEqual(500, self.room.price)

# test_create_room
    # def test_add_room(self):
    #     new_room = Room("80's Room", 10, 1000)
    #     self.room.add_room(new_room)
    #     self.assertEqual(1, len(self.room_list.add_room))

    # def test_find_song(self):
    #     self.song.add_song(self.song)
    #     self.assertEqual(True, self.song.find_song("Believe"))