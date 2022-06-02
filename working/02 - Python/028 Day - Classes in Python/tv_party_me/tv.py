class TV:

    def __init__(self, channel_range, volume_range):

        self.channel_range = channel_range
        self.channel = 0
        self.volume_range = volume_range
        self.volume = 0
        self.power = False

    def turn_on(self):
        self.power = True
        print("TV powering up")

    def turn_off(self):
        self.power = False
        print("TV is powering down")

    def show_powered(self):
        print(f"TV on: {self.power}")

    def channel_up(self, up):
        self.show_channel()
        for push in range(up):
            if self.channel < self.channel_range:
                self.channel += 1
                self.show_channel()

    def channel_down(self, down):
        self.show_channel()
        for push in range(down):
            if self.channel >= 1:
                self.channel -= 1
                self.show_channel()

    def set_channel(self):
        self.show_channel()
        channel = int(input("Choose Channel: >>>"))
        if 1 <= channel <= self.channel_range:
            self.channel = channel
            self.show_channel()
        else:
            print(f"Your TV only has {self.channel_range} channels")
            self.set_channel(self)

    def show_channel(self):
        print(f"Channel: {self.channel}")

    def volume_up(self, up):
        self.show_volume()
        for push in range(up):
            if self.volume < self.volume_range:
                self.volume += 1
                self.show_volume()

    def volume_down(self, down):
        self.show_volume()
        for push in range(down):
            if self.volume >= 1:
                self.volume -= 1
                self.show_volume()

    def show_volume(self):
        print(f"Volume: {self.volume}")
