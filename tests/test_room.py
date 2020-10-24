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