from tv import TV
from channels import Channel
from channels import ChannelManager
from apps import AppManager


if __name__ == '__main__':

    # # Part 1
    #
    # print("***** Part 1 *****")
    # tv = TV(100, 10)
    # tv.turn_on()
    # tv.channel_up(3)
    # tv.volume_up(7)
    # tv.show_channel()
    # tv.show_volume()
    # tv.show_powered()
    # tv.turn_off()
    # tv.show_powered()
    #
    # # Part 2
    # print("***** Part 2 *****")
    # tv.turn_on()
    # tv.set_channel()
    # tv.volume_down(2)
    # tv.show_channel()
    # tv.show_volume()
    # tv.show_powered()

    # Part 3
    print("***** Part 3 *****")
    c = ChannelManager()
    d = AppManager()
    d.add_app()
