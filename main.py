from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from lib.routers.roomRouter import RoomRouter

app = FastAPI()
limiter = FastAPILimiter(key_func=lambda: "anonymous", rate_limits={"anonymous": "10 per minute"})

@app.get("/")
def home():
    return "live response api, by github.com/thullyDev"
    
app.add_middleware(limiter)
room_router = RoomRouter()
app.include_router(room_router.router, prefix="/v1")

# http://localhost:8000/v1/