from fastapi import FastAPI
import uvicorn
from routes import bike_routes


app = FastAPI()
app.include_router(bike_routes)

if __name__ == '__main__':

    # check in browser - http://127.0.0.1:8001/
    uvicorn.run(app='main:app', reload=True, host='127.0.0.1', port=8001)
