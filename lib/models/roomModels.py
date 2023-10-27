from pydantic import BaseModel

class message_room(BaseModel):
    user_id: str
    display_name: str
    room_id: str
    token: str
    message: str

class edit_message(BaseModel):
    user_id: str
    message_id: int
    room_id: str
    token: str
    message: str

class delete_message(BaseModel):
    user_id: str
    message_id: int
    room_id: str
    token: str
