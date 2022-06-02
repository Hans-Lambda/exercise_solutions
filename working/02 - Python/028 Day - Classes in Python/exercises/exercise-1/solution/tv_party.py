from tv import TV

if __name__ == '__main__':
    tv = TV()

    tv.turn_on()
    tv.set_channel(3)
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()

    tv.turn_off()
    tv.turn_on()

    tv.set_channel(95)
    tv.volume_down()
    tv.volume_down()
