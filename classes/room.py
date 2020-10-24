

class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.room_list = []
        self.guest_list = []

    def add_room(self, new_room):
        self.room_list.append(new_room)

    def add_guest(self, new_guest):
        self.guest_list.append(new_guest)
