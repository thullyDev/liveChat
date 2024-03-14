from fastapi import APIRouter
from ..functions.roomFunctions import RoomFunctions
from ..models.roomModels import message_room, edit_message, delete_message, get_room
from ..resources.database import Cache
from ..resources.utilities import (
    SUCESSFUL, 
    NOT_FOUND, 
    FORBIDEEN, 
    CRASH, 
    NOT_FOUND_MSG, 
    SUCESSFUL_MSG, 
    get_uid, 
    get_random_integer_string, 
    get_current_date,
    generate_random_code
)


cache = Cache()

class RoomRouter(RoomFunctions):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(RoomRouter, 
                cls).__new__(cls)
        return cls._instance  
    
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()
        

    def setup_routes(self):
        @self.router.post("/room/")
        def get_room(data: get_room) -> dict:
            room_id = data.room_id
            code = data.room_code
            room_data = cache.dget(room_id)
            room_code = room_data.get("room_code")

            if code != room_code: return self.bad_token({ "message": "the room code is invaild" })

            if not room_data: return self.invaild_room(room_id)

            return self.successful({
                "room": room_id,
                "data": room_data,
             })

        @self.router.get("/room/create/")
        def create() -> dict:
            room_id = get_uid()
            data = {
                "room_id": room_id,
                "room_code": generate_random_code(),
                "created_at": get_current_date(),
                "messages": [],
            }
            cache.dset(room_id, data)

            return self.successful({
                "room": room_id,
                "data": data,
                "message": SUCESSFUL_MSG + ", room will be deleted after 24 hours", 
             })

        # get views, get amount of chatters

        # @self.router.delete("/room/delete/{room_id}/")
        # def delete(room_id: str) -> dict:
        #     cache.delete(room_id)

        #     return self.successful({
        #         "room": room_id,
        #         "data": None,
        #      })

        @self.router.post("/room/message/send")
        def message(data: message_room) -> dict:
            room_id = data.room_id
            code = data.room_code
            user_id = data.user_id
            display_name = data.display_name
            token = data.token
            message = data.message
            user_is_valid = True
            room_data = cache.dget(room_id)
            room_code = room_data.get("room_code")

            if code != room_code: return self.bad_token({ "message": "the room code is invaild" })

            if len(user_id) < 10: return self.bad_token({ "message": "user_id length should be longer then 10" })

            if not room_data: return self.invaild_room(room_id=room_id)

            user_data = cache.dget(user_id)

            if not user_data: 
                display_name = display_name if display_name else "Anon#" + get_random_integer_string()
                user_data = {
                    "display_name": display_name,
                    "user_id": user_id,
                    "created_at": get_current_date(),
                }
                user_is_valid = False

            if user_is_valid and token != user_data.get("token"): return self.bad_token({ "message": "bad token" })

            user_data["token"] = get_uid()
            token = user_data.get("token")

            message_data = {
                "display_name": user_data.get("display_name"),
                "user_id": user_data.get("user_id"),
                "created_at": get_current_date(),
                "message": message,
                "deleted": False,
            }

            room_data["messages"].append(message_data)
            cache.dset(room_id, room_data)
            cache.dset(user_id, user_data)

            return self.successful({
                "room_id": room_id,
                "user_id": user_id,
                "display_name": display_name.get("display_name"),
                "created_at": message_data.get("display_name"),
                "message": message,
                "message_id": len(room_data["messages"]) - 1,
                "token": token,
             })

        @self.router.post("/room/message/edit/")
        def edit_user_message(data: edit_message) -> dict:
            room_id = data.room_id
            code = data.room_code
            user_id = data.user_id
            token = data.token
            message = data.message
            message_id = data.message_id
            room_data = cache.dget(room_id)
            room_code = room_data.get("room_code")

            if code != room_code: return self.bad_token({ "message": "the room code is invaild" })
            if len(user_id) < 10: return self.bad_token({ "message": "user_id length should be longer then 10" })
            if not room_data: return self.invaild_room(room_id=room_id)

            user_data = cache.dget(user_id)

            if not user_data: return self.forbidden()

            if token != user_data.get("token"): return self.bad_token({ "message": "bad token" })

            message_data = {}
            try:
                message_data = room_data["messages"][message_id]
            except IndexError:
                return self.crash({ "message": "no such message" })

            user_data["token"] = get_uid()
            token = user_data.get("token")

            message_data["message"] = message
            message_data["updated_at"] = get_current_date()

            room_data["messages"][message_id] = message_data
            cache.dset(room_id, room_data)
            cache.dset(user_id, user_data)

            return self.successful({
                "room": room_id,
                "user_id": user_id,
                "message": message,
                "message_id": message_id,
                "token": token,
             })

        @self.router.post("/room/message/delete/")
        def delete_user_message(data: delete_message) -> dict:
            room_id = data.room_id
            code = data.room_code
            user_id = data.user_id
            token = data.token
            message_id = data.message_id
            room_data = cache.dget(room_id)
            room_code = room_data.get("room_code")

            if code != room_code: return self.bad_token({ "message": "the room code is invaild" })
            if len(user_id) < 10: return self.bad_token({ "message": "user_id length should be longer then 10" })
            if not room_data: return self.invaild_room(room_id=room_id)

            user_data = cache.dget(user_id)

            if not user_data: return self.forbidden()

            if token != user_data.get("token"): return self.bad_token({ "message": "bad token" })

            message_data = {}
            try:
                message_data = room_data["messages"][message_id]
            except IndexError:
                return self.crash({ "message": "no such message" })

            user_data["token"] = get_uid()
            token = user_data.get("token")

            message_data["deleted"] = True

            room_data["messages"][message_id] = message_data
            cache.dset(room_id, room_data)
            cache.dset(user_id, user_data)

            return self.successful({
                "room": room_id,
                "user_id": user_id,
                "message": message,
                "message_id": message_id,
                "token": token,
             })