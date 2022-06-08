class Channel:

    def __init__(self):

        self.channel_name = None
        self.channel_number = None

    def edit_channel(self, name, number):

        self.channel_name = name
        self.channel_number = number


class ChannelManager:

    def __init__(self):

        self.channels = []

    def add_channel(self):

        print("To setup a new channel, provide name and number")
        name = input("Please provide channel name: ")
        number = input("Please provide channel number: ")
        channel = Channel()
        channel.edit_channel(name, number)
        self.channels.append(channel)


    def delete_channel(self):
        search = input("Which channel do you want to delete?")
        for channel in self.channels:
            if search == str(channel.channel_number) or search in channel.channel_name:
                self.channels.remove(channel)

    def show_channels(self):
        for channel in self.channels:
            print(f"\nName: {channel.channel_name}\nChannel number: {channel.channel_number}\n")

    def reassign_channel(self):
        search = input("Which channel do you want to reassign?")
        for channel in self.channels:
            if search == str(channel.channel_number) or search in channel.channel_name:
                new_place = int(input(f"To which number do you want to reassign {channel.channel_name}? >>> "))
                channel.channel_number = new_place
