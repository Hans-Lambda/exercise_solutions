from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, **kwargs):
        self._mileage_until_next_repair = 200

        kwargs["motorized"] = False
        kwargs["maximum_mileage"] = 600
        kwargs["speed"] = 20
        super().__init__(**kwargs)

    def repair(self):

        print("The "
        + type(self).__name__
        + " has been repaired.")
        self._mileage_until_next_repair = 200

    def drive(self, km: int) -> bool:

        if self._mileage_until_next_repair < 0:
            print(
                "The "
                + type(self).__name__
                + " needs to be repaired before it can go any further."
            )
            return False
        if super().drive(km):
            self._mileage_until_next_repair -= km
            return True
        return False
