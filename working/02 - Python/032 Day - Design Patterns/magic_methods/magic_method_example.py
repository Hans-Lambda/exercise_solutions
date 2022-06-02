class Foods:

    def __init__(self, name, calories, is_fruit):

        self.name = name
        self.calories = calories
        self.is_fruit = is_fruit

    def __dir__(self):
        return self.__dict__.values()
        #return f"{self.name}{str(self.calories)}{str(self.is_fruit)}"


if __name__ == '__main__':

    food = Foods("Mongo", 1000000, True)

    print(food.name)
    print(food.calories)
    print(food.is_fruit)
    print(dir(food))
    #print(dir(Foods))
    #print(food.__dir__())
