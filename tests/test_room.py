import unittest

from classes.room import *
from classes.guest import *
from classes.song import *

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

    def test_remove_guest(self):
        self.guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.add_guest(self.guest)
        self.room.remove_guest("Hannah")
        self.assertEqual(0, len(self.room.guest_list))

    # def test_find_guest(self):
    #     self.assertEqual(False, self.room.find_guest("Hannah"))

    def test_find_guest(self):
        new_guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.add_guest(new_guest)
        self.assertEqual(True, self.room.find_guest("Hannah"))

    def test_checkin_guest_to_room(self):
        self.room = Room("80's room", 10, 1000)
        self.guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.checkin_guest(self.room, self.guest)
        self.assertEqual("Hannah", self.room.guest_list[0].name)

    def test_checkout_guest_from_room(self):
        self.room = Room("80's room", 10, 1000)
        self.guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.checkin_guest(self.room, self.guest)
        self.assertEqual("Hannah", self.room.guest_list[0].name)
        self.room.checkout_guest(self.room, self.guest)
        self.assertEqual(False, self.room.find_guest("Hannah"))

    def test_find_song(self):
        self.new_song = Song("With or Without You", "U2", 4.56, "pop", False)
        self.room = Room("80's room", 10, 1000)
        self.room.add_song_to_room(self.room, self.new_song)
        self.assertEqual(True, self.room.find_song("With or Without You"))

    def test_add_song_to_room(self):
        self.room = Room("80's room", 10, 1000)
        self.song = Song("With or Without You", "U2", 4.56, "pop", False)
        self.room.add_song_to_room(self.room, self.song)
        self.assertEqual("With or Without You", self.room.playlist[0].title)

    def test_remove_song_from_room(self):
        self.room = Room("80's room", 10, 1000)
        self.song = Song("With or Without You", "U2", 4.56, "pop", False)
        self.room.add_song_to_room(self.room, self.song)
        self.assertEqual("With or Without You", self.room.playlist[0].title)
        self.room.remove_song_from_room(self.room, self.song)
        self.assertEqual(False, self.room.find_song("With or Without You"))

    def test_get_guest_wallet(self):
        self.guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.get_guest_wallet(self.guest)
        self.assertEqual(1500, self.guest.wallet)
    
    def test_customer_pay_money(self):
        self.room = Room("80's room", 10, 1000)
        self.guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.customer_pay_money(self.room, self.guest)
        self.assertEqual(500, self.guest.wallet)

    def test_capacity_limit(self):
        self.room = Room("90's room", 4, 1000)
        self.guest = Guest("Hannah", 23, 1500, "We are the Cheeky Girls")
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.assertEqual(4, len(self.room.guest_list))


    def test_guest_fave_song(self):
        self.room = Room("90's room", 4, 1000)
        self.guest = Guest("Hannah", 23, 1500, "With or Without You")
        self.song = Song("With or Without You", "U2", 4.56, "pop", False)
        self.room.add_song_to_room(self.room, self.song)
        self.assertEqual("YASS!", self.room.guest_fave_song(self.guest))

