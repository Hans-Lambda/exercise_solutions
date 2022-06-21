# FastAPI

from fastapi import FastAPI

        app = FastAPI()

        if __name__ == '__main__':

            app.include_router(bike_routes)


        from fastapi import APIRouter
        bike_routes = APIRouter()

check in browser

        http://127.0.0.1:8001/
        http://127.0.0.1:8001/bikes
        http://127.0.0.1:8001/docs

OpenAPI - structure FastAPI
