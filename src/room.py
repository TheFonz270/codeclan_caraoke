class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []
        self.tab = 0
    
    def guest_checkin(self, party):
        self.guest_list = party