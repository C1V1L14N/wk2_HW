import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Dick", 46, 1000, "Believe")

    def test_guest_has_name(self):
        self.assertEqual("Dick", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(46, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(1000, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Believe", self.guest.fave_song)

# test_create_guest
