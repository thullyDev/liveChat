from fastapi import FastAPI
from lib.routers.roomRouter import RoomRouter

app = FastAPI()

@app.get("/")
def home():
    return "live response api, by github.com/thullyDev"

app.include_router(RoomRouter().router, prefix="/v1")