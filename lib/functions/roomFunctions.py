import ast
import json
from ..resources.utilities import SUCESSFUL, NOT_FOUND, FORBIDEEN, CRASH, NOT_FOUND_MSG, SUCESSFUL_MSG
from .globalFunctions import GlobalFunctions

class RoomFunctions(GlobalFunctions):
    def invaild_room(self, room_id=None):
        return self.not_found({
            "room": room_id,
            "message": "this room does not exist", 
         })
         
    # def successful_room(self, data=None, message=SUCESSFUL_MSG, room_id=None):
        # return self.successful({
            # "room": room_id,
            # "data": data,
            # "message": message, 
         # })
