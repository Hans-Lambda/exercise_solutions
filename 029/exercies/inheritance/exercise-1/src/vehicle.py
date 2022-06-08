class Vehicle:

    def __init__(self, **kwargs):
        self.speed = kwargs.get("speed", 100)
        self.maximum_mileage = kwargs.get("maximum_mileage", 100000)
        self.motorized = kwargs.get("motorized", True)

        self.__scrap_metal = False
        print("Ready to go!")

    def drive(self, km: int):

        if self.__scrap_metal:
            print("This " + type(self).__name__ + " can no longer drive.")
            return False
        self.maximum_mileage -= km
        print("The " + type(self).__name__ + " is driving " + str(km) + " km at speed " + str(self.speed) + ".")
        if self.maximum_mileage < 0:
            self.__scrap_metal = True
            print("Unfortunately, your " + type(self).__name__ + " is now scrap metal.")
            return True
        return True
