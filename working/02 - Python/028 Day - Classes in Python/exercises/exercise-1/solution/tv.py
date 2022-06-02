class TV:

    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.is_turned_on = False

    def turn_on(self):
        self.is_turned_on = True
        print(f"TV turned on! {self.is_turned_on}")

    def turn_off(self):
        self.is_turned_on = False
        print(f"TV turned off! {self.is_turned_on}")

    def channel_up(self):
        self.set_channel(self.channel + 1)

    def channel_down(self):
        self.set_channel(self.channel - 1)

    def set_channel(self, channel_number):
        if self.is_turned_on:
            if channel_number > 0 and channel_number <= 100:
                self.channel = channel_number
                print(f"Current Channel is {self.channel}")
            else:
                print("Channel out of range")

    def volume_up(self):
        if self.is_turned_on:
            if self.volume + 1 < 10:
                self.volume += 1
                print(f"Volume is {self.volume}")

    def volume_down(self):
        if self.is_turned_on:
            if self.volume - 1 > 0:
                self.volume -= 1
                print(f"Volume is {self.volume}")

    def switch_on_off(self):
        self.is_turned_on = not self.is_turned_on

