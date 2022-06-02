import random
import uuid
import db
from rent import User, Bike


class BullshitGenerator:

    def __init__(self):

        self.names = ["Franz", "Billy", "Lama", "Mathias"]
        self.usernames = ["blabla69", "creepy69", "fuckup69", "retard69"]
        self.password = ["random", "bullshit", "password", "tooeasy"]
        self.address = ["fuckstreet 69", "IwishIwasanadult 55", "bullshit corner 23", "bush did 911"]

        self.manufacturer = ["myself", "someone else", "I stole it", "no idea"]
        self.types = ["cruiser", "trycycle", "deluxe", "tandem"]

    def generate_user(self):

        user = User()
        user.username = self.usernames[random.randint(0, 3)]
        user.password = self.password[random.randint(0, 3)]
        user.name = self.names[random.randint(0, 3)]
        user.address = self.address[random.randint(0, 3)]
        user.client = True
        user.partner = True

        return user

    def generate_bikes(self, user):

        bike = Bike()

        bike.age = random.randint(1, 25)
        bike.manufacturer = self.manufacturer[random.randint(0, 3)]
        bike.type = self.types[random.randint(0, 3)]
        bike.partner = user
        bike.status = "AVAILABLE"
        bike.id = str(uuid.uuid4())[:5]

        return bike

    def populate(self):

        for i in range(15):
            user = self.generate_user()
            db.users.append(user)
            bike = self.generate_bikes(user)
            db.bikes.append(bike)

        [print(f"{user.username}: {user.password}") for user in db.users]


if __name__ == '__main__':

    bullshit_generator = BullshitGenerator()
    bullshit_generator.populate()
