from fastapi import APIRouter
import controller
from models import Bike

bike_routes = APIRouter()

# if anything is referring to /bikes this will get triggered
@bike_routes.get('/bikes')
def get_bikes():
    return controller.list_bikes()


# not FastAPI standard connotation - just example
# type annotation important
@bike_routes.get('/bikes/by_manufacturer')
def get_bikes_by_manufacturer(manufacturer: str):
    return controller.list_bikes_by_manufacturer(manufacturer)


@bike_routes.get('/bikes/by_name')
def get_bikes_by_name(name: str):
    return controller.list_bikes_by_name(name)


# create entries in application - post to create new bike for example
@bike_routes.post('/bikes')
def post_bikes(bike: Bike):
    controller.add_bike(bike)


# everything in {id} behind /bikes/ gets the id
@bike_routes.delete('/bikes/{id_}')
def delete_bikes(id_: str):
    controller.remove_bike(id_)

