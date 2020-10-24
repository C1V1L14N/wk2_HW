

class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.room_list = []
        self.guest_list = []
        self.playlist = []

    def add_room(self, new_room):
        self.room_list.append(new_room)

    def add_guest(self, new_guest):
        self.guest_list.append(new_guest)

    def remove_guest(self, guest_to_remove):
        for person in self.guest_list:
            if person.name == guest_to_remove:
                self.guest_list.remove(person)

    def find_guest(self, name):
        for person in self.guest_list:
            if person.name == name:
                return True
        return False

    def checkin_guest(self, room, guest):
        self.guest_list.append(guest)

    def checkout_guest(self,room, name):
        self.guest_list.remove(name)

    def add_song_to_room(self, room, song):
        self.playlist.append(song)

    def remove_song_from_room(self, room, song):
        self.playlist.remove(song)

    def find_song(self, name):
        for song in self.playlist:
            if song.name == name:
                return True
        return False

    

   

    
        
             

