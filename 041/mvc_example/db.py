from models import Client
from models import Partner
from models import Bike

clients = [
    Client(1, "Mathias", "some@email", "somestr. 87"),
    Client(2, "Jose", "jose@somewhere", "somestr. 86")
]

partners = [
    Partner("Someone", "some@one", Bike("Type1", "Yamaha", "2010")),
    Partner("Someone Else", "some@else", Bike("Type2", "Honda", "2020")),
]
