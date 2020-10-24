

class Song:
    def __init__(self, title, artist, duration, genre, explicit):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.explicit = explicit
        self.playlist = []
        # self.playlist_1 = [
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     ]
        # self.playlist_2 = [
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     ]
        # self.playlist_3 = [
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     {"title": "xxx", "artist" : "xxx", "duration" : 123, "genre" : "xxx", "explicit" : bool}
        #     ]

    def add_song(self, song):
        self.playlist.append(song)

    def find_song(self, desired_title):
        for song in self.playlist:
            if song.title == desired_title:
                return True
            else:
                return False

    def remove_song(self, song_to_remove):
        for song in self.playlist:
            if song.title == song_to_remove:
                self.playlist.remove(song)