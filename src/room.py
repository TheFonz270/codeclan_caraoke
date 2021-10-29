class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []
        self.tab = 0
    
    def guest_checkin(self, party):
        for person in party:
            self.guest_list.append(person)
        # print(self.guest_list)
    
    def guest_checkout(self, party):
        for person in party:
            self.guest_list.remove(person)
        # print(self.guest_list)