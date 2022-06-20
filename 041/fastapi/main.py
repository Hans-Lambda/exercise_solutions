from fastapi import FastAPI
import uvicorn
from routes import bike_routes


# app related stuff needs to be global to be available
app = FastAPI()
app.include_router(bike_routes)

if __name__ == '__main__':


    # refers to our FastAPI app, uvicorn will reload when code is changed, host is local IP
    # change host to real IP to enable people to use our API

    # check in browser - http://127.0.0.1:8001/
    uvicorn.run(app='main:app', reload=True, host='127.0.0.1', port=8001)

    # Started reloader process [6897] using watchgod // using statreload (Mathias)
