from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lib.routers.roomRouter import RoomRouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "live response api, by github.com/thullyDev"

app.include_router(RoomRouter().router, prefix="/v1")