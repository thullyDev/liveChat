from fastapi import FastAPI
from lib.routers.roomRouter import RoomRouter

app = FastAPI()

@app.get("/")
def home():
    return "live response api, by github.com/thullyDev"

# app.include_router(RoomRouter)
room_router = RoomRouter()
app.include_router(room_router.router, prefix="/v1")

# http://localhost:8000/v1/items/{item_id}