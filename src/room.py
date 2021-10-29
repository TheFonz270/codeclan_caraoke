class Room:
    def __init__(self, capacity, hourly_rate):
        self.capacity = capacity
        self.guest_list = []
        self.play_list = []
        self.entry_fee = 5
        self.hourly_rate = hourly_rate
        self.tab = 0
    
    def check_capacity(self, party):
        return len(party) <= self.capacity
    
    def check_party_covers_entry_fee(self, party):
        for person in party:
            if person.wallet < self.entry_fee:
                return False
        return True

    def guest_checkin(self, party):
        if self.check_capacity(party) and self.check_party_covers_entry_fee(party):
            for person in party:
                self.guest_list.append(person)
                person.wallet -= self.entry_fee
                self.tab += self.entry_fee
        else:
            print("Apologies Party Rejected.")
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
    
    def calculate_tab(self, room):
        total_run_time = 0
        for song in self.play_list:
            total_run_time += song.run_time 
        self.tab += ((total_run_time / 60) /60) * self.hourly_rate