from vehicle import Vehicle


class PublicTransport(Vehicle):

    def __init__(self, **kwargs):
        self.__current_passengers = 0

        kwargs["motorized"] = True
        super().__init__(**kwargs)

    def enter_passengers(self, num: int):

        print(str(num) + " passengers are entering.")
        self.__current_passengers += num

    def exit_passengers(self, num: int):

        print(str(num) + " passengers are exiting.")
        self.__current_passengers -= num

    def get_current_passengers(self) -> int:

        return self.__current_passengers
