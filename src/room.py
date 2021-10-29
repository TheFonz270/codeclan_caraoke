class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guest_list = []
        self.play_list = []
        self.tab = 0
    
    def guest_checkin(self, party):
        for person in party:
            self.guest_list.append(person)
        # print(self.guest_list)
    
    def guest_checkout(self, party):
        for person in party:
            self.guest_list.remove(person)
        # print(self.guest_list)
    
    def add_song(self, song):
        self.play_list.append(song)

    def add_songlist(self, songlist):
        for song in songlist:
            self.play_list.append(song)
    
    def remove_songs(self, song):
        self.play_list.remove(song)
    
    def remove_songlist(self, songlist):
        for song in songlist:
            self.play_list.remove(song)