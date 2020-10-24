import unittest

from classes.room import *
from classes.guest import *

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
    def test_add_room(self):
        new_room = Room("80's Room", 10, 1000)
        self.room.add_room(new_room)
        self.assertEqual(1, len(self.room.room_list))

    # test_create_guest
    def test_add_guest(self):
        new_guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.add_guest(new_guest)
        self.assertEqual(1, len(self.room.guest_list))

    # def test_remove_guest(self):
    #     self.guest.add_guest(self.guest)
    #     self.guest.remove_guest("Dick")
    #     self.assertEqual(0, len(self.guest.guest_list))