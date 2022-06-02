from public_transport import PublicTransport
from bike import Bike


class BikeTaxi(PublicTransport, Bike):

    def __init__(self, motorized, **kwargs):

        kwargs['motorized'] = motorized
        self.max_passengers = 4 if kwargs["motorized"] else 2
        kwargs["speed"] = 30 if kwargs["motorized"] else 18

        super().__init__(**kwargs)

    def enter_passengers(self, num):

        if super().get_current_passengers() + int(num) > self.max_passengers:
            print("Cannot load more passengers at this time.")
        else:
            super().enter_passengers(num)
