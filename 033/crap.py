import random
import uuid
import db
from rent import User, Bike


class BullshitGenerator:

    def __init__(self):

        self.names = ["Franz", "Billy", "Lama", "Mathias"]
        self.usernames = ["Franz69", "Billy69", "Lama69", "Mathias69"]
        self.password = ["random", "bullshit", "password", "tooeasy"]
        self.address = ["fuckstreet 69", "IwishIwasanadult 55", "bullshit corner 23", "bush did 911"]

        self.manufacturer = ["myself", "someone else", "I stole it", "no idea"]
        self.type = ["cruiser", "trycycle", "deluxe", "tandem"]

        self.rng = random.randint(1, 4) - 1

    def generate_user(self):

        user = User()

        self.username = self.usernames[self.rng]
        self.password = self.password[self.rng]
        self.name = self.names[self.rng]
        self.address = self.address[self.rng]
        self.client = True
        self.partner = True

        return user

    def generate_bikes(self, user):

        bike = Bike()

        self.age = random.randint(1, 25)
        self.manufacturer = self.manufacturer[self.rng]
        self.type = self.type[self.rng]
        self.partner = user
        self.status = "AVAILABLE"
        self.id = str(uuid.uuid4())[:5]

        return bike

    def populate(self):

        for i in range(15):
            user = self.generate_user()
            db.users.append(user)
            bike = self.generate_bikes(user)
            db.bikes.append(bike)

        print(f"{db.users.username}: {db.users.password}")
