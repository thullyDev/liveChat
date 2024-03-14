from pydantic import BaseModel

class message_room(BaseModel):
    room_code: str
    user_id: str
    display_name: str
    room_id: str
    token: str
    message: str

class edit_message(BaseModel):
    room_code: str
    user_id: str
    message_id: int
    room_id: str
    token: str
    message: str

class delete_message(BaseModel):
    room_code: str
    user_id: str
    message_id: int
    room_id: str
    token: str

class get_room(BaseModel):
    room_code: str

# class delete_room(BaseModel):
#     room_code: str
