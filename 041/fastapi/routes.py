from fastapi import APIRouter

bike_routes = APIRouter()


# if anything is referring to /bikes this will get triggered
@bike_routes.get('/bikes')
def get_bikes():
    return ["This is the shit I send with my API"]
